class BinaryTree:
    """
    Binary Tree Data Structure
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        values = []

        def walk(root):
            if root is None:
                return "Tree is empty"

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
                return "Tree is empty"

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
                return "Tree is empty"

            if root.left is not None:
                walk(root.left)
            if root.right is not None:
                walk(root.right)
            values.append(root.value)

        walk(self.root)

        return values


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
