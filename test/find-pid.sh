#!/bin/sh
ps aux | grep http-server
echo "-------------------------------------"
lsof -P -i tcp:8080