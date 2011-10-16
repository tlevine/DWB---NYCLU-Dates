#!/bin/bash
echo month,day
cut -d , -f 4 2009.csv|sed -e '1 d' -e '2,$ s/\([0-9][0-9]\)2009/,\1/'
