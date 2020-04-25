FROM node:latest

RUN apt-get update \
    && apt-get install -y unzip \
    && apt-get install -y redis-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /opt/scrumblr
COPY code /opt/scrumblr

WORKDIR /opt/scrumblr
RUN chmod +x start.sh
RUN npm install

VOLUME /var/lib/redis
EXPOSE 8080

ENTRYPOINT [ "./start.sh" ]