#!/bin/python3

import argparse
import os
from typing import Iterator

def load_files(dir: str) -> Iterator[str]:
    pass

def verify(args: argparse.Namespace):
    """Checks if the given path exists

    Args:
        args (argparse.Namespace): argparse results

    Raises:
        FileNotFoundError: When the given path is not a directory
    """
    if not os.path.isdir(args.directory):
        raise FileNotFoundError("Directory not found: {}".format(args.directory))
    
def parse() -> argparse.Namespace:
    """Parses arguments from command line
    """
    parser = argparse.ArgumentParser(\
        description='Counts the number of token types in the directory\'s files')

    parser.add_argument('directory', help='Directory in which to operate the counting')

    parser.add_argument('--time',\
        help="""Whether to time the counting as well. 
        If so, the time is store in a file with suffix \'_time.log\'""",\
            const=True, action='store_const', default=False)
    
    parser.add_argument('--output',\
        help='Name of the file with the token type count per file (default: count_type.log)',\
            default='count_type')

    return parser.parse_args()

def main():
    args = parse()
    verify(args)
    load_files(args.directory)

if __name__ == "__main__":
    main()