class Leaf:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.rec_count = 0
        self.while_count = 0

    def add_using_while(self, value):
        if not self.root:
            self.root = Leaf(value)
        else:
            leaf = self.root
            while True:
                self.while_count += 1
                if leaf.value >= value:
                    if leaf.right is None:
                        leaf.right = Leaf(value)
                        break
                    else:
                        leaf = leaf.right
                else:
                    if leaf.left is None:
                        leaf.left = Leaf(value)
                        break
                    else:
                        leaf = leaf.left

    def add_rec(self, value):

        if not self.root:
            self.root = Leaf(value)
        else:
            self._add_rec(self.root, value)

        print('recursion count:', self.rec_count)

    def _add_rec(self, leaf, value):
        self.rec_count += 1
        if leaf is None:
            return Leaf(value)
        if leaf.value <= value:
            new_leaf = self._add_rec(leaf.right, value)
            leaf.right = new_leaf
        else:
            new_leaf = self._add_rec(leaf.left, value)
            leaf.left = new_leaf
        return leaf


    def in_order(self):
        self._in_order_rec(self.root)

    @classmethod
    def _in_order_rec(cls, node):
        if node is None:
            return

        cls._in_order_rec(node.left)
        print(node.value)
        cls._in_order_rec(node.right)


if __name__ == '__main__':
    t = Tree()
    t.add_using_while(4)
    t.add_using_while(1)
    t.add_using_while(2)
    t.add_using_while(6)
    t.add_using_while(5)
    t.add_using_while(7)
    t.add_using_while(4)

    print('while count', t.while_count)
    t.in_order()

    t = Tree()
    t.add_rec(4)
    t.add_rec(1)
    t.add_rec(2)
    t.add_rec(6)
    t.add_rec(5)
    t.add_rec(7)
    t.add_rec(4)
    print('rec count', t.rec_count)

    t.in_order()




