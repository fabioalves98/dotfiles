#!/bin/sh

cmd="trayer --SetDockType false --widthtype request --align left --edge right --distancefrom right --distance -8 --margin 40 --transparent true --alpha 255 --iconspacing 3"

pgrep -x trayer >/dev/null && pkill trayer|| eval "$cmd" &


