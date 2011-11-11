I wrote some scripts for selecting columns from the data
and cutting them up into smaller files with fewer rows.
The latter will be useful if you can parellize a job across rows.

I also cleaned all of the dates. Here's how you run that.

    $ ./get_data.sh #Download the data and extract it
    $ ./select.sh #Select the date and time columns
    $ ./export_dates-auto.py #Clean the dates and times and send them to json files

The resulting dates are in `data/*-cleantimes.json`.
The "key" refers is the raw time, and the "value" is
the cleaned time.
