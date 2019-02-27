#!/usr/bin/env python3
import sys

from io import parse_input, Output
from solution import algorithm
from output import Output


def main():
    filepath = sys.argv[1]
    data = parse_input(filepath)
    solution = algorithm(data)
    print(Output(solution)[:-1])

if __name__ == '__main__':
    main()
