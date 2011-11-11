#!/bin/bash
slice=$1 #A csv file

#Extract the time information
slice_times="`echo $slice|sed s/\.csv/-times.csv/`"
cut -d , -f 4-5 $slice > $slice_times
