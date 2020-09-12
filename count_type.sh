#!/bin/bash

# Usage
# Input a directory path as an argument.
# Everything inside the directory is counted.
# Output is redirected to two log files.

# Instructions
if [ "$#" != 1 ]; then
	echo "Usage: ./count.sh path-to-a-directory"
	exit 0
fi

# file logs
TIME_OUTPUT='./time_type.log'
COUNT_OUTPUT='./count_type.log'

# initialize empty logs
if test -f "$TIME_OUTPUT"; then
	cat /dev/null > "$TIME_OUTPUT"
else
	touch "$TIME_OUTPUT"
fi

if test -f "$COUNT_OUTPUT"; then
	cat /dev/null > "$COUNT_OUTPUT"
else
	touch "$COUNT_OUTPUT"
fi

# loop through every file in the directory
for file in $1/*
do
	if [ -d "$file" ]; then
		continue
	fi
	/usr/bin/time -o "$TIME_OUTPUT" --append --format='%E' \
	       	cat $file | tr ' ' '\n' | uniq | wc -w \
		>> "$COUNT_OUTPUT"
done
