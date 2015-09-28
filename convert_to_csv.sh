#!/bin/bash
for f in $(find logs/ -type f -name "*.xls*")
do
    echo "Processing $f"
    filename=$(basename "$f")
    filename="${filename%.*}"
    in2csv $f > $(dirname $f)/$filename.csv # convert xls to csv
    env/bin/python csv_cleaner.py $(dirname $f)/$filename.csv # fix bad csv
done
