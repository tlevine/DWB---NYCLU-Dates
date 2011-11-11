#!/usr/bin/env python
"""Export dates to a consistant format. No user input required."""
from export dates import fromfile,tofile

for year in range(2003,2011):
  infile='data/%d-rawtimes.csv' % year
  outfile='data/%d-cleantimes.json' % year
  dts=fromfile(infile,year)
  tofile(dts,outfile)
