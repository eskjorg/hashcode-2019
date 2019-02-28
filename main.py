#!/usr/bin/env python3
import sys

from io_ import parse_input, Output
from solution import algorithm


def main():
    filepath = sys.argv[1]
    photo_collection = parse_input(filepath)
    p = photo_collection.photos[3]
    #solution = algorithm(data)
    #print(Output(solution))


if __name__ == '__main__':
    main()
