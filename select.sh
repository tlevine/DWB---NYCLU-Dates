#!/bin/bash

#Map
for csv in data/20[01][0-9]/slice_[0-9]*.csv
  do
  #nohup ./select-map.sh $csv > $csv.log &
  ./select-map.sh $csv
  echo finished $csv
done
