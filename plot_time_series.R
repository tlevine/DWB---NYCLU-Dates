library(ggplot2)
# Plot stops over time.
# WARNING: This ignores time bins without stops.

remove_weirdness<-function(tmp){
  subset(tmp,interval>0)
}

import<-function(){
  dfs<-list()
  plots<-list()
  for (interval in c('hours','days')){
    for (year in as.character(2003:2010)){
      tmp<-read.csv(paste(
        'datetime_bins/',year,'-',interval,'.csv'
      ,sep=''),colClasses=rep('numeric',2))
      tmp<-remove_weirdness(tmp)
  
      dfs[interval][[1]]<-rbind(dfs[interval][[1]],tmp)
    }
    dfs[interval][[1]]$interval<-as.POSIXct(
       dfs[interval][[1]]$interval,origin='1970-01-01'
    )
    plots[interval][[1]]<-ggplot(
        dfs[interval][[1]],aes(interval,count)
      ) +
      geom_line() + xlab("Time")
  }
  list(
    dfs=dfs
  , plots=plots
  )
}

plot_sqf<-list(
  typical_week=function(sqf,year=NA){
    if (!is.na(year)){
      sqf$dfs$hours<-subset(
        sqf$dfs$hours
      , strftime(interval,format='%Y')==as.character(year)
      )
    } else if (length(year)==2) {
      years<-as.numeric(strftime(sqf$dfs$hours$interval,format='%Y'))
      sqf$dfs$hours<-subset(
        sqf$dfs$hours
      , years>year[1]&years<year[2]
      )
    }
    foo<-strftime(sqf$dfs$hours$interval,format='%a %H:00')
    bar<-sqf$dfs$hours$count 
    baz<-aggregate(bar,list(foo),mean)
    names(baz)<-c('hour','count')
    labelsep<-seq(1,nrow(baz),12)
    baz$index=1:nrow(baz)

    partial_plot<- ggplot(baz,aes(index,count)) +
      scale_x_continuous(
        breaks=baz$index[labelsep]
      , labels=baz$hour[labelsep]
      ) +
      geom_line() + ylab("Stops per hour")
    if (is.na(year)){
      partial_plot+xlab("The average week across the whole dataset")
    } else {
      partial_plot+xlab(paste('The average week in',year))
    }
  }
, hours=function(sqf){
    print(sqf$plots$hours +
     ylab("Stops per hour")
    )
  }
, days=function(sqf){
    print(sqf$plots$days +
     ylab("Stops per day")
    )
  }
)

sqf<-import()

go<-function(){
  pdf('sqf.pdf',width=17,height=11)
  plot_sqf$days(sqf)
  print(plot_sqf$typical_week(sqf,c(2003,2005))+ylim(0,200))
  print(plot_sqf$typical_week(sqf,c(2006,2010))+ylim(0,200))
  for (year in 2003:2005){
    print(plot_sqf$typical_week(sqf,year)+ylim(0,1500))
  }
  for (year in 2006:2010){
    print(plot_sqf$typical_week(sqf,year)+ylim(0,200))
  }
  dev.off()
}
