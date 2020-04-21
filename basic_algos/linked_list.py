
class LinkedList:
    class LinkedListNode:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next = next_node
        def __repr__(self):
            return f'{type(self).__name__}({self.value})'

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, element):
        new = self.LinkedListNode(element)
        if self.head is None:
            self.head = new

        if self.tail is None:
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def enumerate(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def reverse(self):
        node = self.head
        prev_node = None
        while node:
            node.next, prev_node, node = prev_node, node, node.next
        self.head, self.tail = self.tail, self.head

    @property
    def is_empty(self):
        if self.head is None and self.tail is None:
            return True
        return False

    def pop(self):

        if not self.is_empty:
            node = self.head
            if node.next is None and node == self.tail:
                self.tail = None
                self.head = None
                return node

            while node.next != self.tail:
                node = node.next
            node.next = None
            pop_node = self.tail
            self.tail = node
            return pop_node

    def remove(self, index):
        idx = 0
        prev_element = None
        for el in self.enumerate():
            if idx == index:
                if prev_element is None:
                    self.head = el.next
                else:
                    prev_element.next = el.next
                if el == self.tail:
                    self.tail = prev_element

            prev_element = el
            idx += 1

    def __repr__(self):
        return str(list(self.enumerate()))




if __name__ == '__main__':

    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    for el in ll.enumerate():
        print(el.value)

    print('*'*10)

    ll.reverse()

    for el in ll.enumerate():
        print(el.value)

    print('*' * 10)

    while not ll.is_empty:
        el = ll.pop()
        print(el.value)

    print('removing', '*' * 10)
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    ll.remove(0)

    for el in ll.enumerate():
        print(el.value)

    print(str(ll))