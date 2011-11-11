#!/usr/bin/env python
"""Export dates to a consistant format. No user input required."""
from export_dates import fromfile

def increment(d,key):
  if not key in d.keys():
    d[key]=0
  d[key]=d[key]+1

def main():
  from json import dumps
  d=extract()
  
  #JSON
  json=dumps(d)
  f=open('datetime_bins.json','w')
  f.write(json)
  f.close()

  #CSV
  for interval in ('hours','days'):
    f=open('datetime_bins-%s.csv' % interval,'w+')
    f.write('interval,count')
    for key in d[interval]:
      f.write('%d,%d' % (key,d[interval][key])
    f.close()

def extract():
  hours={}
  hour=3600
  days={}
  day=24*hour
  for year in range(2003,2011):
    infile='data/%d-rawtimes.csv' % year
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
