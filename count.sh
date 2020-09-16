#!/bin/bash

python count_type.py /u/demorali/corpora/1g-word-lm-benchmark-r13output/training-monolingual.tokenized.shuffled/ --time --count types

python graph.py types.csv --image types.png --xlabel "Nombre de tranche lue" \
    --ylabel "Nombre de types" --title "Nombre de types vs. nombre de tranche lue"

python graph.py types_time.csv --image types_time.png --xlabel "Nombre de tranche lue" \
    --ylabel "Temps écoulé (s)" --title "Temps écoulé vs. nombre de tranche lue"
