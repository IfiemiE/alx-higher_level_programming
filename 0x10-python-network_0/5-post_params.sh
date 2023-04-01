#!/bin/bash
# POST method new Header variables (and values) to Server
curl -sX POST -d "email:test@gmail.com&subject:I will always be here for PLD" $1
