# IFT 6285: Devoir 1
All scripts must be run on the DIRO machines in order to access the corpus.

# Required components
* `bash` and `python3`
* GNU time for timing
* matplotlib for plotting

# Usage
## Counting words
`./count.sh folder` will create two log files named `count.log` and `time.log`. Each line on the log files represents the word count and time taken to count of a file in the given folder. 

`./count_type.sh folder` behaves in a similar way, but produces `count_type.log` and `time_type.log` instead. The word count is now of the token types (how many different words).

## Visualization
`./graph.py` will read a given file and produce a `png` image of a graph. Use `-h` for help on how to use it.