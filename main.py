#!/usr/bin/env python3
import sys

from io_ import parse_input

from solution import algorithm

# from test_output import algorithm
from combine_slideshows import combine_slideshows


def main():
    filepath = sys.argv[1]
    photo_collection = parse_input(filepath)

    #slideshow = algorithm(photo_collection)
    #print(slideshow)

    slideshows = algorithm(photo_collection)

    merged_slideshow = combine_slideshows(slideshows)
    print(merged_slideshow)


if __name__ == '__main__':
    main()
