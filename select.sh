#!/bin/bash

if [ "" = "$1" ]
#  then files=data/20[01][0-9]/slice_[0-9]*.csv
  then files='data/[0-9]*.csv'
else
  files="$1"
fi

#Map
for csv in $files
  do
  #nohup ./select-map.sh $csv > $csv.log &
  ./select-map.sh $csv
  echo finished $csv
done

#./select-reduce.sh
