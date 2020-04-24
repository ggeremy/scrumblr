#!/bin/bash

cd /opt/scrumblr
service redis-server start && node server.js --port 8080 --redis redis://127.0.0.1:6379