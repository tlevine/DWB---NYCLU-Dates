fromcsv<-function () {
  days<-read.csv('dates-cleaner.csv')
  h<-hist((356*days$year)+(days$month-1)*30+days$day,plot=F,breaks=363*7)
  pdf(width=85,height=11)
  plot(h$counts~h$mids,type='l',axes=F,ylab="Stops per day",xlab="Day");axis(1);axis(2)
  dev.off()
}

fromposix<-function () {
  stops.messy<-table(read.csv('dates-posix.csv',header=F)$V1)
  stops<-stops.messy[stops.messy>0]
  day<-as.POSIXlt(names(stops),origin='1970-1-1')
  
  pdf(width=85,height=11)
  plot(stops~day
  , type='l',axes=F
  , ylab="Stops per day"
  , xlab="Day"
  , main="Stops over time"
  )
  axis(1);axis(2)
  dev.off()
}
