#!/bin/bash
echo year,month,day
for file in *.csv
  do
  year=`basename $file .csv`
  cut -d , -f 4 $file|sed -e 's/^/'$year',/' -e 's/"//g'| sed -e '1 d' -e '2,$ s/\([0-9][0-9]\)'$year'/,\1/'
done
