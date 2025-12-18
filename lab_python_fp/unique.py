class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.used_elements = set()

    def __next__(self):
        while True:
            item = next(self.items)
            val = item.lower() if self.ignore_case and isinstance(item, str) else item

            if val not in self.used_elements:
                self.used_elements.add(val)
                return item

    def __iter__(self):
        return self


if __name__ == '__main__':
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data)))
    print(list(Unique(data, ignore_case=True)))
