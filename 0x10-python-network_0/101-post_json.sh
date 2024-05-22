#!/bin/bash
# Sends a JSON POST request to URL passed as 1st arg, and displays response's body.
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
