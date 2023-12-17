class ArrayList:
    def __init__(self):
        self.data = []
        self.length = 0

    def __iter__(self):
        for item in self.data:
            yield item

    def add(self, item):
        self.data = self.data + [item]
        self.length += 1

    def get_length(self):
        return self.length

    def get(self, index):
        if 0 <= index < self.length:
            return self.data[index]

    def set(self, index, value):
        if 0 <= index < self.length:
            self.data[index] = value
