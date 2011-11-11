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

def tofile(d): 
  #CSV
  print 'Making csv files'
  for interval in ('hours','days'):
    f=open('datetime_bins-%s.csv' % interval,'w+')
    f.write('interval,count')
    for key in d[interval]:
      f.write('%d,%d\n' % (key,d[interval][key]))
    f.close()

  #JSON
  print 'Making a json file'
  json=dumps(d)
  f=open('datetime_bins.json','w')
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
