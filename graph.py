"""Grapher

Produces simple graphs from single column csv files,
by taking them as Y values and by using a 0-to-size count
as X values.

Arguments allow the naming of axes and titles.
"""
import csv
import argparse
from typing import List, Dict
import numpy as np

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def graph(data: List[float], subject: Dict, out='graph.png'):
    """Generates a graph from the given data and axes labels

    Args:
        data (List[float]): Read csv data
        subject (Dict): Titles and axes
        out (str, optional): Name of the image. Defaults to 'graph.png'.
    """
    # uses matplotlib to graph
    x_values = np.arange(0, len(data))
    y_values = data
    plt.plot(x_values, y_values)

    # Import labels from dictionary
    plt.xlabel(subject['xlabel'])
    plt.ylabel(subject['ylabel'])
    plt.title(subject['title'])

    plt.savefig(out)

    # debug info
    print("Max value of the graph is {data_max} and data size is {data_size}."
          .format(data_max=data[-1], data_size=len(data)))


def read_file(path: str) -> List[float]:
    """Reads the file into a list of numbers

    Args:
        path (str): Path to the csv file

    Returns:
        List[float]: Data to be graphed
    """
    data: List[float] = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=' ', quotechar='|')
        for row in reader:
            head, *_ = row
            data.append(float(head))

    return data


def parse() -> argparse.Namespace:
    """Parses the command line arguments

    Returns:
        argparse.Namespace: Parsed arguments
    """
    # command line interface
    parser = argparse.ArgumentParser(
        description='Graph the csv file made of just one column')

    # csv
    parser.add_argument('csv',
                        help='Csv file to graphed.')

    # image output
    parser.add_argument('--image', metavar='image.png', default='graph.png',
                        help='Output picture name (default: graph.png)')

    # titles, axes labels
    parser.add_argument('--xlabel', default='',
                        help='Name of the x axis')
    parser.add_argument('--ylabel', default='',
                        help='Name of the y axis')
    parser.add_argument('--title', default='',
                        help='Title of the plot')

    args = parser.parse_args()
    return args


def main():
    """Parses the file and then graphs it with the given arguments
    """
    args = parse()

    # read csv file
    data = read_file(args.csv)

    # produce graph
    labels = {
        'xlabel': args.xlabel,
        'ylabel': args.ylabel,
        'title': args.title
    }
    graph(data, subject=labels, out=args.image)


if __name__ == "__main__":
    main()
