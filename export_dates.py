#!/usr/bin/env python
"""Export dates to a consistant format."""
from parse_dates import parse_line
from json import dumps

class InvalidFileFormat(Exception):
  pass

def fromfile(filename,year,keys=True):
  """Get the datetime objects from a file"""
  csv=open(filename)
  out=[]
  for line in csv:
    dt=parse_line(line,year)
    if keys:
      out.append({"key":line,"value":dt})
    else:
      out.append({"value":dt})
  return out

def tofile(dts,filename,fileformat='json',timeformat='%s'):
  """Output to a file. Default format is POSIX time."""
  for dt in dts:
    dt['value']=dt['value'].strftime(timeformat)

  out=open(filename,'w')
  if 'json'==fileformat:
    out.write(dumps(dts))
  else:
    raise InvalidFileFormat

if __name__ == "__main__":
  #print fromfile('data/2004/slice_014-times.csv',2004,keys=True)
  #print fromfile('data/2004/slice_014-times.csv',2004)
  dts=fromfile('data/2004/slice_014-times.csv',2004)
  tofile(dts,'foo.json')
