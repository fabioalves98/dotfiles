#!/bin/bash

STATUS=$(playerctl -p spotify status 2>/dev/null)
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo $STATUS
else
    echo "No player is running"
fi