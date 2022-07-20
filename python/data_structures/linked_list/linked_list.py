

class TargetError(Exception):
    pass


class LinkedList:
    """
    Linked list class
    Has `head` property
    """

    def __init__(self, head=None):
        self.head = head

    def __bool__(self):
        return self.head != None

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
            if current == None:
                raise TargetError
            new_node = Node(new_value)
            current = self.head
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
            if current.next == None:
                raise TargetError
            new_node = Node(new_value)
            current = self.head
            while current:
                if current.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next
        except:
            raise TargetError

    def kth_from_end(self, num):
        if self.head == None:
            raise TargetError
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        if num >= length or num < 0:
            raise TargetError
        length = length - (num + 1)
        while length != 0 and self.head:
            self.head = self.head.next
            length -= 1
        return self.head.value


class Node:
    """
    Data Node for Linked List class
    Has `value` and `next` attributes
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


if __name__ == "__main__":
    node3 = Node(3)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    ll = LinkedList(node1)
    ll.kth_from_end(3)
