#!/bin/bash

if [ "x$1" == "x" ]; then
    docker build --tag=board:latest .
fi

if [ "x$1" == "xrun" ]; then
    docker stop $(docker ps -a -q)
    docker rm $(docker ps -a -q)
    docker build --tag=board:latest .
    docker run -p 8080:8080 -v `pwd`/redis:/var/lib/redis board:latest
fi

if [ "x$1" == "xrund" ]; then
    docker stop $(docker ps -a -q)
    docker rm $(docker ps -a -q)
    docker build --tag=board:latest .
    docker run -p 8080:8080 -v `pwd`/redis:/var/lib/redis -d board:latest
fi

