
class BinaryTree:
    """
    Binary Tree Data Structure
    """

    def __init__(self, root=None):
        self.root = root
        self.max_value = float('-inf')

    def pre_order(self):
        values = []

        def walk(root):
            if root is None:
                return

            values.append(root.value)
            if root.left is not None:
                walk(root.left)
            if root.right is not None:
                walk(root.right)

        walk(self.root)

        return values

    def in_order(self):
        values = []

        def walk(root):
            if root is None:
                return

            if root.left is not None:
                walk(root.left)
            values.append(root.value)
            if root.right is not None:
                walk(root.right)

        walk(self.root)

        return values

    def post_order(self):
        values = []

        def walk(root):
            if root is None:
                return

            if root.left is not None:
                walk(root.left)
            if root.right is not None:
                walk(root.right)
            values.append(root.value)

        walk(self.root)

        return values

    # Using list from pre_order method

    # def find_maximum_value(self):
    #     values = self.pre_order()
    #     max_value = values[0]
    #     for value in values:
    #         if value > max_value:
    #             max_value = value
    #     return max_value

    # Using BFT

    # def find_maximum_value(self):
    #     q = [self.root]
    #     _max = float('-inf')
    #     while len(q) > 0:
    #         node = q.pop(0)
    #         if node:
    #             q.append(node.left)
    #             q.append(node.right)
    #             _max = max(_max, node.value)
    #     return _max

    # Using modified pre_order method

    # def find_maximum_value(self):
    #     self.pre_order()
    #     return self.max_value

    # Creating new methods

    def traverse(self, root):
        if root is None:
            return
        if root.value > self.max_value:
            self.max_value = root.value
        if root.left is not None:
            self.traverse(root.left)
        if root.right is not None:
            self.traverse(root.right)

    def find_maximum_value(self):
        self.traverse(self.root)
        return self.max_value


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
