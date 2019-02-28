"""Parse input file into data structure."""


class InputData:
    """First line of the input file."""
    def __init__(self, n_items, field1, field2):
        self.n_items = int(n_items)
        self.field1 = field1
        self.field2 = field2
        # self.rows = 0
        # self.columns = 0
        # self.n_vehicles = 0
        # self.n_rides = 0
        # self.rides = []
        # self.bonus = 0
        # self.steps = 0
        self.items = []


class InputItem:
    """One row of the input file."""
    def __init__(self, field1):
        self.field1 = field1
        # self.start = [0,0]
        # self.end = [0,0]
        # self.earliest_start = 0
        # self.latest_finish = 0
        # self.index = 0
        #
        # self.distance = 0
        # self.max_allowed_time = 0
        # self.buffer_time = 0


def parse_input(input_file):
    with open(input_file, 'r') as f:

        first_line = f.readline()
        tokens = first_line.split(' ')
        input_data = InputData(*tokens)

        for i in range(input_data.n_items):
            tokens_item = f.readline().split(' ')
            item = InputItem(*tokens_item)
            input_data.items.append(item)

    return input_data


class Output:
    """Format for printing to file."""
    def __init__(self, solution):
        self.items = solution

    def __str__(self):
        output = ''
        for item in self.items:
            output += '{} {}\n'.format(len(item.members), str(item))

        return output
