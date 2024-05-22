#!/bin/bash
# Sends request to URL passed as an arg, and displays the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
