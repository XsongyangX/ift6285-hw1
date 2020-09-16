#!/bin/python3

import argparse
import os, sys
from typing import Iterator, Dict
import subprocess
import csv, json
import time

def read_words(path: str) -> Iterator[str]:
    """Reads a file and give an iterator over its words

    Args:
        file (str): File name

    Yields:
        Iterator[str]: Generator over the file's words
    """
    try:
        with open(path, 'r') as file:
            for line in file:
                for word in line.split():
                    yield word
    except OSError as error:
        print(error, file=sys.stderr)    

def load_files(dir: str) -> Iterator[str]:
    """Returns a generator iterating on the text file names only

    Args:
        dir (str): directory of interest on disk

    Yields:
        Iterator[str]: Generator over the file names with full path
    """
    for file in os.listdir(dir):
        path = os.path.join(dir, file)

        # ignore directories
        if os.path.isdir(path):
            continue

        # ignore binary files
        process = subprocess.Popen(['file', '--mime', path], stdout=subprocess.PIPE, text=True)
        mime, error = process.communicate()
        if error is not None:
            print(error, file=sys.stderr)
        if 'charset=binary' in mime:
            continue

        yield path

def verify(args: argparse.Namespace):
    """Checks if the given path exists

    Args:
        args (argparse.Namespace): argparse results

    Raises:
        FileNotFoundError: When the given path is not a directory
    """
    if not os.path.isdir(args.directory):
        raise FileNotFoundError("Directory not found: {}".format(args.directory))

class Log:
    """Log object controling the generation of results into files
    """
    def __init__(self, output:str, records_time: bool=False):
        self.__count_stream = open("{}.csv".format(output), 'w', newline='')
        self._count = csv.writer(self.__count_stream, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if records_time:
            self.__time_stream = open("{}_time.csv".format(output), 'w', newline='')
            self._time = csv.writer(self.__time_stream, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            self._time_start = time.time()

    def __del__(self):
        self.__count_stream.close()
        if hasattr(self, '__time_stream'):
            self.__time_stream.close()

    def log_time(self):
        """Logs the time of the execution so far
        """
        if hasattr(self, '_time'):
            self._time.writerow([time.time() - self._time_start])

    def log_types(self, types: int):
        """Logs the number of types read until now

        Args:
            types (int): Number of types read
        """
        self._count.writerow([types])

    def log_vocabulary(self, vocabulary: Dict, json_name: str):
        """Writes the vocabulary to a json file

        Args:
            vocabulary (Dict): Vocabulary dictionary
            json_name (str): Name of the json file
        """
        with open("{}.json".format(json_name), 'w') as file:
            json.dump(vocabulary, file)

def parse() -> argparse.Namespace:
    """Parses arguments from command line
    """
    parser = argparse.ArgumentParser(\
        description='Counts the number of token types in the directory\'s files')

    parser.add_argument('directory', help='Directory in which to operate the counting')

    parser.add_argument('--time',\
        help="""Whether to time the counting as well. 
        If so, the time is store in a file with suffix \'_time.csv\'""",\
            const=True, action='store_const', default=False)
    
    parser.add_argument('--count',\
        help='Name of the file (without extension) for the token type count per file (default: count_type.csv)',\
            default='count_type')

    parser.add_argument('--json',\
        help='Name of the json (without extension) of the vocabulary (default: vocabulary.json)',\
            default='vocabulary')


    return parser.parse_args()

def main():
    args = parse()
    verify(args)
    files = load_files(args.directory)

    # initiate log files for time and count
    log = Log(args.count, args.time)

    # initiate empty dictionary and counter
    vocabulary = dict()
    count = 0
    types = 0

    # populate dictionary
    for file in files:
        for word in read_words(file):
            count += 1
            if word in vocabulary:
                vocabulary[word] += 1
            else:
                vocabulary[word] = 1
                types += 1

        log.log_types(types=types)
        if args.time is True:
            log.log_time()

    
    # produce a json vocabulary
    log.log_vocabulary(vocabulary=vocabulary, json_name=args.json)

    # final message
    print(\
        """Finished counting:
        {word_count} words in total
        {type_count} types in total
        """.format(word_count=count, type_count=types))
    

if __name__ == "__main__":
    main()