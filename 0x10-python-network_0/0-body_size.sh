#!/bin/bash
# Sends a request to input URL and display size of the body of response
curl -s $1 | wc -c
