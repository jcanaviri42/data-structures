class MyArray:
    def __init__(self):
        self.collection = []
        self.length = 0

    def size(self):
        return self.length

    def is_empty(self):
        return self.size() == 0

    def get(self, index):
        return self.collection[index]

    def set(self, new_value, index):
        self.collection[index] = new_value
        self.length += 1

    def clear(self):
        self.collection = []
        self.length = 0

    def add(self, new_value):
        self.collection.append(new_value)
        self.length += 1

    def remove_at(self, index):
        """Removes an element, by its index"""
        del self.collection[index]
        self.length -= 1

    def remove(self, value):
        """Removes an element, by its value"""
        for index, item in enumerate(self.collection):
            if item == value:
                del self.collection[index]
                self.length -= 1

    def index_of(self, value):
        for index, item in enumerate(self.collection):
            if item == value:
                return index

    def exists(self, value):
        return value in self.collection

    def __repr__(self):
        if self.length == 0:
            return "[ ]"

        string_items = [str(item) for item in self.collection]
        return f"[ {', '.join(string_items)} ]"


a = MyArray()

assert a.size() == 0
assert a.is_empty()

print(a)

a.add(5)
a.add(4)
a.add(3)
a.add(2)
a.add(1)

print(a)

assert a.size() == 5

print(a.get(3))

assert not a.exists(14)
assert a.exists(1)

a.remove(5)
a.remove_at(0)
print(a)

assert a.size() == 3
