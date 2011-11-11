#!/usr/bin/env python

def test(year):
  csv=open('time_format/%d' % year)
  for line in csv:
    print parse_line(line,year)

def parse_line(line,year):
  """Parse the date and time from a raw line of
  the csv file for a given year."""
  raw=split_time(line,year)
  return parse_date(raw,year)

def parse_date(raw,year):
  if year in (2003,2004):
    return parse_date_0304(raw)
  if year in (2005,2009,2010):
    return parse_date_050910(raw)
  if year==2006:
    return parse_date_06(raw)
  if year in (2007,2008):
    return parse_date_0708(raw)
  else:
    return raw

def parse_date_0304(d):
  return d

def parse_date_050910(d):
  return d

def parse_date_06(d):
  return d

def parse_date_0708(d):
  return d

def split_time(dateline,year):
  """Split the time into a dict of year and time."""
  dateline=dateline.replace('\n','')
  if year in (2003,2004,2005):
    time,date=dateline.split(',')
  else:
    date,time=dateline.split(',')
  return {
    "date":date
  , "time":time
  }

if __name__ == "__main__":
  for year in range(2003,2011):
    test(year)
