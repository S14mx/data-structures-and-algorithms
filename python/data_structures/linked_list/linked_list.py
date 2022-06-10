
class TargetError(Exception):
    pass


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

    def append(self, value):
        new_node = Node(value)
        current = self.head
        while current:
            if current.next == None:
                current.next = new_node
                break
            current = current.next

    def insert_before(self, value, new_value):
        try:
            new_node = Node(new_value)
            current = self.head
            if current == None:
                raise TargetError
            while current:
                if current.value == value:
                    new_node.next = current
                    self.head = new_node
                elif current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next
        except:
            raise TargetError

    def insert_after(self, value, new_value):
        try:
            new_node = Node(new_value)
            current = self.head
            if current.next == None:
                raise TargetError
            while current:
                if current.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next
        except:
            raise TargetError

    def kth_from_end(value):
        pass


class Node:
    """
    Data Node for Linked List class
    Has `value` and `next` attributes
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
