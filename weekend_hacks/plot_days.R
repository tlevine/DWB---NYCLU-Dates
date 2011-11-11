fromcsv<-function (filename) {
  days<-read.csv(filename)
  h<-hist((356*days$year)+(days$month-1)*30+days$day,plot=F,breaks=363*7)
  pdf(width=85,height=11)
  plot(h$counts~h$mids,type='l',axes=F,ylab="Stops per day",xlab="Day");axis(1);axis(2)
  dev.off()
}

fromposix<-function () {
  stops.messy<-table(read.csv('dates-posix.csv',header=F)$V1)
  stops<-unlist(stops.messy[
    stops.messy>0
  ])
#  & as.numeric(names(stops.messy))<as.numeric(strptime('2010-01-01',format='%Y-%m-%d'))
#  ]
  day<-as.POSIXlt(as.numeric(names(stops)),origin='1970-01-01',tz="EST")
  
  pdf(width=85,height=11)
  plot(day,stops
  , type='l',axes=F
  , ylab="Stops per day"
  , xlab="Day"
  , main="Stops over time"
  )
  axis(1);axis(2)
  dev.off()
  stops
}
