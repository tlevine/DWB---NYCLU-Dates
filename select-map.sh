#!/bin/bash
csv=$1 #A csv file

#Extract the time information
csv_times="`echo $csv|sed s/\.csv/-rawtimes.csv/`"
cut -d , -f 4-5 $csv > $csv_times

#Remove header if there is one
stop=`sed -n '1 p' $csv_times|grep -i --only-matching stop|tr A-Z a-z`
if [ "$stop" != "" ]
  then sed -i '1 d' $csv_times
fi
