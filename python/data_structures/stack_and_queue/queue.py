from data_structures.stack_and_queue.node import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    Class for node based Queue data structure
    """

    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def is_empty(self):
        if not self.front:
            return True

    def peek(self):
        if not self.front:
            raise InvalidOperationError
        return self.front.value

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError
        temp = self.front
        if self.front.next:
            self.front = self.front.next
            temp.next = None
        else:
            self.front = None
        return temp.value
