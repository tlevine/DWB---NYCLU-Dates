#!/bin/bash

#Defaults
if [ "" = "$1" ]
  then lines_per_file=10000
else
  lines_per_file=$1
fi
 
#Map
for csv in data/*.csv
  do
  year=`basename $csv .csv`
  nohup ./slice-map.sh data/$year $lines_per_file > data/$year.log &
done
