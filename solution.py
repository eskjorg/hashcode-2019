"""Algorithms."""
from itertools import cycle
import numpy as np
from util import SlideShow, Slide


class OutputItem(object):
    """Item representing row in output file."""

    def __init__(self):
        self.members = []
        #self.time_counter = 0
        #self.position = [0,0]
        #self.last_visited_index_sorted = 0

    def __str__(self):
        """Output format"""
        return ' '.join([str(x) for x in self.members])


def algorithm(input_data):
    solution = []

    verticals = set()
    horizontals = set()
    for image in input_data.photos:
        if image.orientation == 'V':
            verticals.add(image)
        else:
            horizontals.add(image)

    # Add horizontals
    slideshow = [SlideShow(Slide(photo)) for photo in horizontals]

    # Add verticals
    if len(verticals) > 0:
        avg_vert_size = avg_tag_size(verticals)
        vert_slideshow = list(pair_verticals(verticals, avg_vert_size))
        slideshow = slideshow + vert_slideshow

    return slideshow


def pair_verticals(verticals, avg_vert_size):
    vert_temp = list(verticals)
    vert_temp = sorted(vert_temp)
    NUM_BINS = min([50, len(vert_temp)])
    vert_temp_list_of_cycles = list(chunks(vert_temp, NUM_BINS))
    for i in range(int(NUM_BINS / 2)):
        print(i)
        first_bin = vert_temp_list_of_cycles[i]
        last_bin = vert_temp_list_of_cycles[NUM_BINS-1-i]
        for photo1 in first_bin:
            costs = [cost_vertical_pair(photo1, photo2, avg_vert_size) for photo2 in last_bin]
            amin = np.argmin(costs)
            photo2 = last_bin.pop(amin)
            yield SlideShow(Slide(photo1, photo2))




def chunks(l, n_bins):
    size = int(len(l) / n_bins)
    for i in range(0, len(l), size):
        #yield cycle(l[i:i + size])
        yield list(l[i:i + size])

def avg_tag_size(set1):
    tag_sizes = [photo.size for photo in set1]
    return sum(tag_sizes) / len(tag_sizes)


def cost_vertical_pair(v1, v2, avg):
    is_avg = abs(avg - (v1.size + v2.size) / 2.0)
    inter = len(set(v1.tags).intersection(set(v2.tags)))
    return is_avg + 4 * inter
