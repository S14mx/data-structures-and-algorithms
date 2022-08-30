from data_structures.tree.binary_tree import BinaryTree
from data_structures.stack_and_queue.queue import Queue
from data_structures.hash_table.hashtable import Hashtable


def tree_intersection(tree1, tree2):
    if type(tree1) != type(BinaryTree()) or type(tree2) != type(BinaryTree()):
        return "Invalid input. Only Binary trees are allowed as arguments"
    if not tree1.root or not tree2.root:
        return []

    q = Queue()
    hash_table = Hashtable()
    result = set()
    q.enqueue(tree1.root)

    while not q.is_empty():
        dequeued = q.dequeue()
        if not hash_table.contains(dequeued.value):
            hash_table.set(dequeued.value, True)
        if dequeued.left:
            q.enqueue(dequeued.left)
        if dequeued.right:
            q.enqueue(dequeued.right)

    q.enqueue(tree2.root)
    while not q.is_empty():
        dequeued = q.dequeue()
        if hash_table.contains(dequeued.value):
            result.add(dequeued.value)
        if dequeued.left:
            q.enqueue(dequeued.left)
        if dequeued.right:
            q.enqueue(dequeued.right)
    return result


if __name__ == "__main__":
    bt = BinaryTree()
    print(type(bt) == type(BinaryTree()))
