# Modify gittag appropriately
%define gittag  96e0a0
%define instdir %{nodejs_sitelib}/scrumblr

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

%description
Web-based simulation of a physical agile sprint board that supports real-time
collaboration.

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p -m 755 $RPM_BUILD_ROOT%{instdir}
tar -C $RPM_BUILD_ROOT%{instdir}/ --strip-components=1 -xf %{SOURCE0}

# Remove unwanted files
find $RPM_BUILD_ROOT%{instdir} -name '.git*' -o -name '.node*' | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%post
pushd %{instdir}
npm install
popd

%files
%defattr(-,root,root,-)
%dir %{instdir}
%{instdir}/*

%changelog
* Thu Dec 28 2014 Adam Tkac <adam.tkac@gooddata.com>
- initial package
