#!/usr/bin/env python3
import sys

from io_ import parse_input
from test_output import algorithm


def main():
    filepath = sys.argv[1]
    photo_collection = parse_input(filepath)
    slideshow = algorithm(photo_collection)
    print(slideshow)
    print('tot:', slideshow.total_score)


if __name__ == '__main__':
    main()
