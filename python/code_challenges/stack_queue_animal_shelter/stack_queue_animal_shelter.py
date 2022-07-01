from data_structures.stack_and_queue.queue import Queue
from data_structures.stack_and_queue.node import Node


class AnimalShelter:
    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()

    def enqueue(self, animal):
        if animal.value == "cat":
            self.cat_queue.enqueue(animal)
        if animal.value == "dog":
            self.dog_queue.enqueue(animal)
        else:
            return "Sorry, only cats and dogs allowed"

    def dequeue(self, animal):
        if animal == "cat":
            return self.cat_queue.dequeue()
        if animal == "dog":
            return self.dog_queue.dequeue()
        else:
            return None


class Dog(Node):
    def __init__(self, value="dog"):
        super().__init__(value)


class Cat(Node):
    def __init__(self, value="cat"):
        super().__init__(value)
