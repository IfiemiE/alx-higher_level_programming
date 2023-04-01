#!/bin/bash
# Sends a request to the input URL and display the allowable merhods of the server
curl -sI $1 | grep -i "allow"
