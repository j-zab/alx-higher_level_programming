#!/bin/bash
# sends a POST request to a passed URL using curl, and display the response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
