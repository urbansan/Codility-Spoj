import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        # print(root.data)
        current_nodes = [root]
        while current_nodes:
            next_lvl_nodes = []
            for node in current_nodes:
                print(node.data, end=' ')
                next_lvl_nodes.append(node.left) if node.left else None
                next_lvl_nodes.append(node.right) if node.right else None
            current_nodes = next_lvl_nodes




# Write your code here
def get_tree(T):
    # T = int(input())
    myTree = Solution()
    root = None
    for data in T:
        root = myTree.insert(root, data)
    return myTree, root


tree, root = get_tree([3, 5, 4, 7, 2, 1])
tree.levelOrder(root)
