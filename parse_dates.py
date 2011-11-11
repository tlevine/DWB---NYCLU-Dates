#!/usr/bin/env python

def test(year):
  csv=open('times_head.csv')
  for line in csv:
    print parse_line(line,year)
    return None

def parse_line(line,year):
  """Parse the date and time from a raw line of
  the csv file for a given year."""
  raw=split_time(line,year)
  return parse_date(raw,year)

def parse_date(raw,year):
  if year in (2003,2004):
    return parse_date_0304(raw)

def parse_date_0304(d):
  return d

def split_time(dateline,year):
  """Split the time into a dict of year and time."""
  if year in (2003,2004,2005):
    time,date=dateline.split(',')
  else:
    date,time=dateline.split(',')
  return {
    "date":date
  , "time":time
  }

if __name__ == "__main__":
  test(2003)
