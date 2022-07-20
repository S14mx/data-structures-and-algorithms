
from data_structures.kary_tree import KaryTree, Node
from data_structures.stack_and_queue.queue import Queue


def fizz_buzz_value(value):
    if value % 3 == 0 and value % 5 == 0:
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
    else:
        return str(value)


# using BFT
# def fizz_buzz_tree(tree):
#     new_tree = KaryTree()
#     new_tree.root = Node()
#     q = Queue()
#     q.enqueue((tree.root, new_tree.root))

#     while not q.is_empty():
#         old_node, new_node = q.dequeue()
#         new_node.value = fizz_buzz_value(old_node.value)

#         for child in old_node.children:
#             new_child_node = Node()
#             new_node.children.append(new_child_node)
#             q.enqueue((child, new_child_node))

#     return new_tree


# using recursion
def fizz_buzz_tree(tree):
    new_tree = KaryTree()

    def clone(node):
        if node is None:
            return

        node_clone = Node(fizz_buzz_value(node.value))
        for child in node.children:
            child_clone = clone(child)
            node_clone.children.append(child_clone)

        return node_clone
    new_tree.root = clone(tree.root)
    return new_tree
