#!/bin/bash
# displays HTTP methods accepted by the server using curl.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
