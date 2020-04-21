class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node




start = Node(1, Node(2, Node(3, Node(4))))

# node = start
# while node:
#     print(node.value)
#     node = node.next

prev_node = None
node = start
while node:
    print(node.value)
    node.next, node, prev_node = prev_node, node.next, node

while prev_node:
    print(prev_node.value, prev_node.next)
    prev_node = prev_node.next

# print(start.next)