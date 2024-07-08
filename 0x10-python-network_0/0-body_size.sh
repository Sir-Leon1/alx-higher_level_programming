#!/bin/bash
# Get the byte size of the HTTP response for a given URL
curl -s "$1" | wc -c
