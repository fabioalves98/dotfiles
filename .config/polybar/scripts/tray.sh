#!/bin/sh

pgrep -x stalonetray >/dev/null && pkill stalonetray|| eval stalonetray &
