class LinkedList:
    """
    Linked list class
    Has `head` property
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = Node(value)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        output_string = ""
        current = self.head
        while current:
            output_string += f"{{ {current.value} }} -> "
            current = current.next
        output_string += "NULL"
        return output_string


class Node:
    """
    Data Node for Linked List class
    Has `value` and `next` attributes
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    pass
