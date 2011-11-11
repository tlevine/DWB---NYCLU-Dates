#!/usr/bin/env python
from datetime import datetime
from pytz import timezone

def test(year):
  csv=open('time_format/%d' % year)
  for line in csv:
    parse_line(line,year)

def parse_line(line,year):
  """Parse the date and time from a raw line of
  the csv file for a given year."""
  raw=split_time(line,year)
  return parse_date(raw,year)

def parse_date(raw,year):
  if year in (2003,2004):
    d=parse_date_0304(raw)
  elif year in (2005,2009,2010):
    d=parse_date_050910(raw)
  elif year==2006:
    d=parse_date_06(raw)
  elif year in (2007,2008):
    d=parse_date_0708(raw)
  else:
    print 'fail'

  print d

  #Time zone
  #year,month,day,hour,minute=d
  year,month,day,hour,minute=[2004,3,5,3,1]
  return datetime(year,month,day,hour,minute,tzinfo=timezone('EST'))

def parse_date_0304(d):
  mmddyyyy=d['date'].replace('"','')
  return mmddyyyy

def parse_date_050910(d):
  mmddyyyy='%08d' % int(d['date'])
  return mmddyyyy

def parse_date_06(d):
  l=d['date'].split('-')
  l.reverse()
  mmddyyyy=''.join(l)
  return mmddyyyy

def parse_date_0708(d):
  mmddyyyy=d['date']
  return mmddyyyy

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
