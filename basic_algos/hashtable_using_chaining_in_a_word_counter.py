from binascii import crc32
from basic_algos.linked_list import LinkedList

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __repr__(self):
        return f'{type(self).__name__}({self.value})'

class Hashtable:
    fill_factor = 0.75
    default_size = 2
    def __init__(self):
        self._size = self.default_size
        self._store = [None] * self._size

    def _get_index(self, key) -> int:
        hash_ = crc32(key.encode())
        index = hash_ % self._size
        return index

    def add(self, key: str, value):
        index = self._get_index(key)
        new_node = Node(key, value)
        if self._store[index] is None:
            self._store[index] = LinkedList()

        self._store[index].append(new_node)


    def find(self, key):
        index = self._get_index(key)
        for el in self._store[index].enumerate():
            if el.value.key == key:
                return el.value.value

    def update(self, key, value):
        index = self._get_index(key)
        for el in self._store[index].enumerate():
            if el.value.key == key:
                el.value.value = value

    def items(self):
        for idx in range(self._size):
            ll = self._store[idx]
            if ll is not None:
                for el in ll.enumerate():
                    yield el.value.key, el.value.value

    def remove(self, key, value):
        pass

if __name__ == '__main__':
    ht = Hashtable()

    ht.add('ball', 4)
    ht.add('guitar', 10)
    ht.add('tv', 20)
    ht.add('table', 4)



    for key, value in ht.items():
        print(key, value)

    cost = ht.find('ball') + 20
    ht.update('ball', cost)
    print(ht.find('ball'))