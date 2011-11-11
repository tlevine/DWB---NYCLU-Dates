#!/bin/bash
# Run this after generating the slices.
#
# (I don't know how to figure out when the generation is done
# except by checking the logs)

#List of all headers
cat data/20[01][0-9]/head.csv > headers.csv
