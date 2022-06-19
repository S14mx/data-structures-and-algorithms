
from data_structures.stack_and_queue.node import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    """
    Class for node based Stack data structure
    """

    def __init__(self, top=None):
        self.top = top

    def is_empty(self):
        if not self.top:
            return True

    def peek(self):
        if not self.top:
            raise InvalidOperationError
        return self.top.value

    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if not self.top:
            raise InvalidOperationError
        temp = self.top
        if self.top.next:
            self.top = self.top.next
            temp.next = None
        else:
            self.top = None

        return temp.value
