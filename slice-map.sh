#!/bin/bash
year=$1
lines_per_file=$2

if [ "" = "$year" ] || [ "" = "$lines_per_file" ]
  then echo You need to specify both the year and the number of lines per file.
else
  echo slice
fi

function slice {
  #Make a folder for the year
  mkdir $year

  #Extract the header
  sed -n '1 p' $year.csv > $year/head.csv

  #Split into many slices
  split -l $lines_per_file -a 3 -d $year.csv slice_
  for s in slice_[0-9]*
    do mv $s $s.csv
  done

  #Remove the header row from the first slice
  sed -i '1 d' slice_000.csv
}
