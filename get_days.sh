#!/bin/bash
cut -d , -f 4 2009.csv|sed 's/\([0-9][0-9]2009$\)/,\1/'
