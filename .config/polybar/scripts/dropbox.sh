#!/bin/sh

case "$1" in
    --toggle)
        pgrep -x dropbox >/dev/null && pkill -f dropbox || dropbox start
        ;;
    *)
        echo " $(dropbox status)"
        ;;
esac