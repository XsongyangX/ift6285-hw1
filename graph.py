#!/bin/python3
import argparse
from typing import List, TypeVar
import numpy as np

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from numbers import Real

def graph(data: List[Real], subject='count', out='graph.png'):
    # debug info
    print("Max value of the graph is {data_max} and data size is {data_size}."\
        .format(data_max=data[-1], data_size=len(data)))
    
    # uses matplotlib to graph
    x = np.arange(0, len(data))
    y = data
    plt.plot(x,y)

    # Change the text here if you wish to edit labels on the graph
    plt.xlabel("Nombre de tranche lus")

    if subject == 'count':
        plt.ylabel("Nombre de mots")
        plt.title("Nombre de mots en fonction du nombre de tranche")
    elif subject == 'time':
        plt.ylabel("Temps pris (s)")
        plt.title("Temps pris en fonction du nombre de tranche lue")
    elif subject == 'unique':
        plt.ylabel("Nombre de mots différents")
        plt.title("Nombre de types en fonction du nombre de tranche")

    plt.savefig(out)

def process(data: List[Real]) -> List[Real]:
    
    # cumulatively sum the data
    cum_data : List[Real] = []
    for element in data:
        try:
            cum_data.append(cum_data[-1] + element)
        except IndexError: # for the first element
            cum_data.append(element)

    return cum_data

def read_file(path: str, subject: str ='count') -> List[Real]:
    
    data : List[Real] = []
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if subject == 'time':
                data.append(float(line))
            else:
                data.append(int(line))

    return data

def main():
    # command line interface
    parser = argparse.ArgumentParser(\
        description='Graph the log files from the counting scripts')
    
    parser.add_argument('log',\
        help='Log file to graphed.')

    topic_group = parser.add_mutually_exclusive_group()

    topic_group.add_argument('--time', dest='subject', action='store_const',\
        const='time', default='count',\
            help='Makes the graph labels to be for time (default: count)')

    topic_group.add_argument('--unique', dest='subject', action='store_const',\
        const='unique', default='count',\
            help='Makes the graph labels to be about token types (default: count)')

    parser.add_argument('--output', nargs='?', dest='out',\
        help='Output picture name')

    args = parser.parse_args()

    # data analysis
    data = read_file(args.log, subject=args.subject)
    data = process(data)
    if args.out is not None:
        graph(data, subject=args.subject, out=args.out)
    else:
        graph(data, subject=args.subject)

if __name__ == "__main__":
    main()
