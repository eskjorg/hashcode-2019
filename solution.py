"""Algorithms."""

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
