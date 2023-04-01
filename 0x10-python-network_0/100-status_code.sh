#!/bin/bash
# sends a request & displays only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
