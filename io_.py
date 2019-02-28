"""Parse input file into data structure."""


class PhotoCollection:
    """First line of the input file."""
    def __init__(self, n_photos):
        self.n_photos = int(n_photos)
        self.photos = []


class Photo:
    """."""
    def __init__(self, id, orientation, tags):
        self.id = id
        self.orientation = orientation
        self.tags = tags
        self.size = len(tags)

    def __lt__(self, other):
        return self.size < other.size

    @property
    def n_tags(self):
        return len(self.tags)


def parse_input(input_file):
    with open(input_file, 'r') as f:

        n_photos = f.readline()
        input_data = PhotoCollection(n_photos)

        for i in range(input_data.n_photos):
            tokens_item = f.readline().split(' ')

            tokens_item[-1] = tokens_item[-1][0:-1]
            item = Photo(i, tokens_item[0], {item for item in tokens_item[2:]})
            input_data.photos.append(item)
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
