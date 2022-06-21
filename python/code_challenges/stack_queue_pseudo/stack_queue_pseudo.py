
from data_structures.stack_and_queue.stack import Stack


class PseudoQueue(Stack):

    def enqueue(self, value):
        temp_stack = PseudoQueue()
        while not self.is_empty():
            temp_stack.push(self.pop())
        self.push(value)
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

    def dequeue(self):
        if not self.is_empty():
            return self.pop()
