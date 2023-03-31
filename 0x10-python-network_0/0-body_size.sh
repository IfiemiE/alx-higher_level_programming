#!/bin/bash
# Sends a request to input URL and display size of the body of response
curl -sI $1 | grep -i content-length |grep -Eo [0-9]
