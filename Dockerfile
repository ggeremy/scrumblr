FROM node:latest

RUN mkdir /opt/scrumblr
COPY code /opt/scrumblr
WORKDIR /opt/scrumblr

RUN apt-get update \
    && apt-get install -y unzip \
    && apt-get install -y redis-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && npm install

VOLUME /var/lib/redis
EXPOSE 8080

ENTRYPOINT [ "./start.sh" ]