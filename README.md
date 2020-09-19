# IFT 6285: Devoir 1
All scripts must be run on the DIRO machines in order to access the corpus.

# Required components
* `bash` and `python3`
* GNU time for timing
* matplotlib for plotting

# Usage
## Counting words
`./count.sh` will call the `count_type.py` and `graph.py` scripts with the correct arguments for the 1B-word corpus. 

`./count_type.py folder [options]` counts all readable non-binary files inside the folder and generates type counts, timing and vocabulary at the end. Use `-h` for help.

## Visualization
`./graph.py csv [options]` will read a given csv file and produce a `png` image of a graph. Use `-h` for help on how to use it.