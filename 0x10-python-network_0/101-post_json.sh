#!/bin/bash
#script that sends a JSON POST request to a URL passed as the first argument
curl -s "$1" -X POST --json cat "$2"
