#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_ that gets message "You got me!"
curl -sL -X PUT -H "Origin:" -d "user_id=98" 0.0.0.0:5000/catch_me
