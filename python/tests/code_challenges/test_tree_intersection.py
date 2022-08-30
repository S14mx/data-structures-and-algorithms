import pytest
from code_challenges.tree_intersection.tree_intersection import tree_intersection
from data_structures.tree.binary_tree import BinaryTree, Node
from data_structures.stack_and_queue.queue import Queue


def test_exists():
    assert tree_intersection


def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)


def test_tree_intersection_invalid_input():

    bt = BinaryTree()
    tree_intersection(bt, [])
    expected = "Invalid input. Only Binary trees are allowed as arguments"
    assert expected


def test_tree_intersection_tree_empty():

    bt1 = BinaryTree()
    bt2 = BinaryTree()
    values = [1, 2, 3]
    add_values_to_empty_tree(bt1, values)
    actual = tree_intersection(bt1, bt2)
    expected = []
    assert actual == expected


def test_tree_intersection_no_matches():

    bt1 = BinaryTree()
    bt2 = BinaryTree()
    values1 = [1, 2, 3]
    values2 = [4, 5, 6]
    add_values_to_empty_tree(bt1, values1)
    add_values_to_empty_tree(bt2, values2)
    actual = tree_intersection(bt1, bt2)
    expected = set()
    assert actual == expected


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)


def test_tree_intersection_invalid_input():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)
