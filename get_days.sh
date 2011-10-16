#!/bin/bash
echo year,month,day> dates.csv
for file in 200*.csv
  do
  year=`basename $file .csv`
  cut -d , -f 4 $file|tr -d '"'|sed -e 's/^/'$year',/' -e '1 d' -e '2,$ s/\([0-9][0-9]\)'$year'/,\1/' >> dates.csv
done

cat dates.csv| grep -e ',.*,' > dates-cleaner.csv

rm dates-posix.csv
for d in `head dates-cleaner.csv|tr , -`
  do date -d $d +%s >> dates-posix.csv
done
