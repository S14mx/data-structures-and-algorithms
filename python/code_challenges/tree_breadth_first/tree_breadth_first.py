from data_structures.tree.binary_tree import BinaryTree
from data_structures.stack_and_queue.queue import Queue


def breadth_first(tree):
    values = []
    q = Queue()
    q.enqueue(tree.root)

    while not q.is_empty():
        popped = q.dequeue()

        if popped is not None:
            values.append(popped.value)

            if popped.left is not None:
                q.enqueue(popped.left)

            if popped.right is not None:
                q.enqueue(popped.right)

    return values
