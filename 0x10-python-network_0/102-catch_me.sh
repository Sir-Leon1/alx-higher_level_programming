#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_ that gets message "You got me!"
curl -s 0.0.0.0:5000/catch_me -X GET -H "Origin: HolbertonSchool" -d "user_id=98" -o /dev/null -w "You got me!"
