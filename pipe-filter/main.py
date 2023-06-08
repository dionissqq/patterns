import random


# Filter
class Filter:
    def process(self, data):
        raise NotImplementedError("Subclasses must implement the process method")


# Filters
class FilterUpperCase(Filter):
    def process(self, data):
        return data.upper()


class FilterReverse(Filter):
    def process(self, data):
        return data[::-1]


class FilterShuffle(Filter):
    def process(self, data):
        chars = list(data)
        random.shuffle(chars)
        return ''.join(chars)


# Pipe
class Pipe:
    def __init__(self):
        self.filters = []

    def add_filter(self, filter):
        self.filters.append(filter)

    def process_data(self, data):
        for filter in self.filters:
            data = filter.process(data)
        return data


if __name__ == '__main__':
    pipe = Pipe()

    # Create and add filters to the pipe
    pipe.add_filter(FilterUpperCase())
    pipe.add_filter(FilterReverse())
    pipe.add_filter(FilterShuffle())

    # Process data through the pipe
    data = "Pipe-Filter Pattern"
    result = pipe.process_data(data)

    print(f"Input data: {data}")
    print(f"Output data: {result}")
