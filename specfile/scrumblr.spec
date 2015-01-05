# Modify gittag appropriately
%define gittag  XXXXXX
%define instdir %{nodejs_sitelib}/scrumblr

%if 0%{?rhel} > 6 || 0%{?fedora}
%global initscript 0
%else
%global initscript 1
%endif

Name:           scrumblr
Version:        0.2.0
Release:        0.1.%{gittag}%{?dist}
Summary:        Web-based simulation of a physical agile sprint board

Group:          Applications/Internet
License:        GPLv3+
URL:            https://github.com/vaclavbohac/scrumblr

BuildArch:      noarch

# Create this way from git:
# git archive --format=tar --prefix=scrumblr-0.2.0-git%{gittag}/ HEAD |gzip > scrumblr-0.2.0-git%{gittag}.tar.gz
Source0:        %{name}-%{version}-git%{gittag}.tar.gz

BuildRequires:  nodejs-packaging
Requires:       nodejs, npm
%if %{initscript}
Requires:       daemonize
Requires(post): chkconfig
Requires(preun):chkconfig
# This is for /sbin/service
Requires(preun):initscripts
Requires(postun):initscripts
%endif

%description
Web-based simulation of a physical agile sprint board that supports real-time
collaboration.

%prep
%setup -q -n %{name}-%{version}-git%{gittag}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p -m 755 $RPM_BUILD_ROOT%{instdir}
tar -C $RPM_BUILD_ROOT%{instdir}/ --strip-components=1 -xf %{SOURCE0}

# Remove unwanted files
find $RPM_BUILD_ROOT%{instdir} -name '.git*' -o -name '.node*' | xargs rm -f

# Init script
%if %{initscript}
mkdir -p $RPM_BUILD_ROOT%{_initddir}
install -m 755 scrumblr.init $RPM_BUILD_ROOT%{_initddir}/scrumblr
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
pushd %{instdir}
npm install
popd
%if %{initscript}
/sbin/chkconfig --add %{name}
%endif

%if %{initscript}
%preun
if [ $1 -eq 0 ] ; then
    /sbin/service %{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi

%postun
if [ "$1" -ge "1" ] ; then
    /sbin/service %{name} condrestart >/dev/null 2>&1 || :
fi
%endif

%files
%defattr(-,root,root,-)
%dir %{instdir}
%{instdir}/*
%if %{initscript}
%{_initddir}/scrumblr
%endif

%changelog
* Thu Dec 28 2014 Adam Tkac <adam.tkac@gooddata.com>
- initial package
