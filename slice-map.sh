#!/bin/bash
yeardir=$1
lines_per_file=$2

if [ "" = "$yeardir" ] || [ "" = "$lines_per_file" ]
  then echo You need to specify both the year directory and the number of lines per output file.
else
  echo slice
  sleep 1h
  echo finished
fi

function slice {
  #Make a folder for the yeardir
  mkdir $yeardir

  #Extract the header
  sed -n '1 p' $yeardir.csv > $yeardir/head.csv

  #Split into many slices
  split -l $lines_per_file -a 3 -d $yeardir.csv $yeardir/slice_
  for s in $yeardir/slice_[0-9]*
    do mv $s $s.csv
  done

  #Remove the header row from the first slice
  sed -i '1 d' $yeardir/slice_000.csv
}
