#!/bin/sh

case "$1" in
    --toggle)
        pgrep -x dropbox >/dev/null && pkill -f dropbox || dropbox start
        ;;
    *)
        echo " $(maestral status | grep Status | xargs | awk -F "Status " '{print $2}')"
        ;;
esac
