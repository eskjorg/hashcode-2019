#!/usr/bin/env python3
import sys

from io_ import parse_input

from solution import algorithm

# from test_output import algorithm
from combine_slideshows import combine_slideshows
from combine_hash import combine_hash


def main():
    filepath = sys.argv[1]
    photo_collection = parse_input(filepath)

    #slideshow = algorithm(photo_collection)
    #print(slideshow)

    slideshows = algorithm(photo_collection)

    #merged_slideshow = combine_slideshows(slideshows)
    merged_slideshow = combine_hash(slideshows)
    print(merged_slideshow)


if __name__ == '__main__':
    main()
