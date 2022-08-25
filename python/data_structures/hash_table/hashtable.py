from data_structures.linked_list.linked_list import LinkedList, Node


class Hashtable:
    """
    Hash table data structure
    """

    def __init__(self, size=1024) -> None:
        self.size = size
        self._buckets = [None] * size

    def set(self, key: str or int, value: any) -> None:
        """ This method hashes the key, and adds the key and value pair to the table, in case of a collision the most recent key is added to the end of linked list

            Arguments: key, value

        """

        if (type(key) != str) and (type(key) != int):
            return "Only strings or integers are allowed as keys"

        node = Node({key: value})
        if not self._buckets[self.hash(key)]:
            self._buckets[self.hash(key)] = LinkedList(node)
        else:
            current = self._buckets[self.hash(key)].head
            while current.next:
                current = current.next
            current.next = node

            while current:
                current = current.next

    def get(self, key: str) -> any:
        """ Returns a value associated with the key in the table

            Arguments: key
        """
        if type(key) != str and type(key) != int:
            return "Only strings or integers are allowed as keys"

        try:

            current = self._buckets[self.hash(key)].head
            while current:
                if key in current.value.keys():
                    return current.value[key]
                current = current.next
            return "Key is not found"

        except:
            return "Key is not found"

    def contains(self, key: str) -> bool:
        """Returns a Boolean, indicating if the key exists in the table already.

        Arguments: key
        """
        if type(key) != str and type(key) != int:
            return "Only strings or integers are allowed as keys"

        try:

            current = self._buckets[self.hash(key)].head
            while current:
                if key in current.value.keys():
                    return True
                current = current.next
            return False

        except:
            return False

    def keys(self):
        collection = []
        for item in self._buckets:
            if item:
                current = item.head
                while current:
                    collection += current.value.keys()
                    current = current.next
        return collection

    def hash(self, key):
        """Returns an Index in the collection for the given key

        Arguments: key
        """
        if type(key) != str and type(key) != int:
            return "Only strings or integers are allowed as keys"

        hashed_key = 0

        for character in str(key):
            hashed_key += ord(character)

        primed = hashed_key * 21

        hashed_key = primed % self.size
        return hashed_key
