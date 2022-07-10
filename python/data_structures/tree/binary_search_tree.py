from data_structures.tree.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Class for BinarySearchTree data structure
    """

    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return

        def walk(root, node):

            if not root:
                return

            if node.value < root.value:
                if root.left:
                    walk(root.left, node)
                else:
                    root.left = node
            else:
                if root.right:
                    walk(root.right, node)
                else:
                    root.right = node

        walk(self.root, node)

    def contains(self, value):
        found = []

        def walk(root):
            if not root:
                return

            if root:
                if value == root.value:
                    found.append(value)
                else:
                    if value < root.value:
                        if root.left:
                            walk(root.left)
                    else:
                        if root.right:
                            walk(root.right)

        walk(self.root)
        return len(found) == 1
