#!/usr/bin/env python
from parse_dates import *

def testyears():
  for year in range(2003,2011):
    testyear(year)

def testyear(year):
  csv=open('time_format/%d' % year)
  for line in csv:
    print parse_line(line,year)

if __name__ == "__main__":
  testyears()
