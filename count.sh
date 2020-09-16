#!/bin/bash

python count_type.py /u/demorali/corpora/1g-word-lm-benchmark-r13output/training-monolingual.tokenized.shuffled/ --time --count types

python graph.py types.csv --image types.png --xlabel
