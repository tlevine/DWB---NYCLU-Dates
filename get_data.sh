#!/bin/bash

URL='http://thomaslevine.com/nyclu-data.tar.gz'

#Download and decompress the source data files
wget $URL
tar xvzf `basename $URL`
