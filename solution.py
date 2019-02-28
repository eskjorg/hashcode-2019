"""Algorithms."""


class SlideShow:

    def __init__(self):
        pass


class Slide:

    def __init__(self, photo1, photo2=None):
        self.ids = {photo1.id}
        self.tags = {*photo1.tags}

        if photo2 is not None:
            if photo1.orientation != 'V' and photo2.orientation != 'V':
                raise ValueError('2 photos in a slide needs to be vertical.')
            self.ids.union(photo2.id)
            self.tags.union(photo2.tags)
        elif photo1.orientation != 'H':
            raise ValueError('single photo slide need horizontal photo.')


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
    # TODO: Implement solution here
    for i in range(2):
        item = OutputItem()
        for j in range(3):
            item.members.append(i * j)
        solution.append(item)
    return solution
