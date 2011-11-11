#!/usr/bin/env python

def test():
  csv=open('times_head.csv')
  for line in csv:
    print line

def parse_line(line,year):
  """Parse the date and time from a raw line of
  the csv file for a given year."""

def split_time(dateline):
  if year<=2005:
    time,date=dateline.split(',')
  else:
    date,time=dateline.split(',')
  return {
    "date":date
  , "time":time
  }

def parse_time_0304(dateline):
  
