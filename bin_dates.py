#!/usr/bin/env python
"""Export dates to a consistant format. No user input required."""
from export_dates import fromfile
from json import dumps

def increment(d,key):
  if not key in d.keys():
    d[key]=0
  d[key]=d[key]+1

def main():
  for year in range(2003,2011):
    year=year
    d=extract(year=year)
    'Finished extracting'
    tofile(d,str(year))

def tofile(d,year='all'): 
  #CSV
  print 'Making csv files'
  for interval in ('hours','days'):
    f=open('datetime_bins/%s-%s.csv' % (year,interval),'w+')
    f.write(interval+',count\n')
    for key in d[interval]:
      f.write('%d,%d\n' % (key,d[interval][key]))
    f.close()

  #JSON
  print 'Making a json file'
  json=dumps(d)
  f=open('datetime_bins/%s.json' % year,'w')
  f.write(json)
  f.close()

def extract(start=2003,end=2011,year=None):
  hours={}
  hour=3600
  days={}
  day=24*hour
  if year!=None:
    start=year
    end=year+1
  for year in range(start,end):
    infile='data/%d-rawtimes.csv' % year
    print 'Extracting from %s' % infile
    dts=fromfile(infile,year)
    dt_objs=[row['value'] for row in dts]
 
    for dt in dt_objs:
      posix=int(dt.strftime('%s'))
      # int truncates rather than rounds
      increment(hours,int(posix/hour)*hour)
      increment(days,int(posix/day)*day)
  return {"hours":hours,"days":days}

if __name__ == "__main__":
  main()
