#!/usr/bin/env python
from datetime import datetime
from pytz import timezone

def parse_line(line,year):
  """Parse the date and time from a raw line of
  the csv file for a given year."""
  raw=split_time(line,year)
  return parse_datetime(raw,year)

def parse_datetime(raw,year):
  #Date
  if year in (2003,2004):
    mmddyyyy=parse_date_0304(raw['date'])
  elif year in (2005,2009,2010):
    mmddyyyy=parse_date_050910(raw['date'])
  elif year==2006:
    mmddyyyy=parse_date_06(raw['date'])
  elif year in (2007,2008):
    mmddyyyy=parse_date_0708(raw['date'])
  else:
    print 'fail'

  #Time
  if year in (2003,2004,2005):
    hhmm=parse_time_030405(raw['time'])
  elif year in (2005,2006,2007,2008,2009,2010):
    hhmm=parse_time_0607080910(raw['time'])
  else:
    print 'fail'

  return datetime_fromstring(mmddyyyy,hhmm)

def datetime_fromstring(mmddyyyy,hhmm):
  """Create a datetime object with the appropriate time zone
  from two strings."""
  month=int(mmddyyyy[0:2])
  day=int(mmddyyyy[2:4])
  year=int(mmddyyyy[4:8])

  hour=int(hhmm[0:2])
  minute=int(hhmm[2:4])
  return datetime(year,month,day,hour,minute,tzinfo=timezone('EST'))

def parse_time_030405(raw):
  """Let's put in a dummy time because I don't know how it works."""
  return '0000'

def parse_time_0607080910(raw):
  return raw

def parse_date_0304(raw):
  mmddyyyy=raw.replace('"','')
  return mmddyyyy

def parse_date_050910(raw):
  mmddyyyy='%08d' % int(raw)
  return mmddyyyy

def parse_date_06(raw):
  l=raw.split('-')
  l.reverse()
  mmddyyyy=''.join(l)
  return mmddyyyy

def parse_date_0708(raw):
  return raw

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
  testyears()
