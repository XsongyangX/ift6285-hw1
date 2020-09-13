#!/bin/python3
import argparse

import matplotlib.pyplot as plt
import numpy as np

def read_file(path: str, subject='time'):
    
    data = []
    with open(path, 'r') as file:
        for line in file:
            if subject == 'time':
                data.append(int(line))

def main():
    parser = argparse.ArgumentParser(\
        description='Graph the log files from the counting scripts')
    
    parser.add_argument('log',\
        help='Log file to graphed.')

    parser.add_argument('--time', )

    args = parser.parse_args()

    read_file(args.log, subject='time')

if __name__ == "__main__":
    main()
