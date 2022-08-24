from data_structures.linked_list.linked_list import LinkedList, Node


class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def set(self, key, value):

        # set
        # Arguments: key, value
        # Returns: nothing
        # This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

        node = Node({key: value})
        if not self._buckets[self.hash(key)]:
            self._buckets[self.hash(key)] = LinkedList(node)
        else:
            current = self._buckets[self.hash(key)].head
            print(current.value)
            while current.next:
                current = current.next
            current.next = node

    def get(self, key):
        pass

        # get
        # Arguments: key
        # Returns: Value associated with that key in the table

    def contains(self, key):
        pass

        # contains
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.

    def keys(self):
        pass

        # keys
        # Returns: Collection of keys

#     'roger' 10431 list: 1024
    def hash(self, key):

        # hash
        # Arguments: key
        # Returns: Index in the collection for that key

        hashed_key = 0

        for character in str(key):
            hashed_key += ord(character)

        primed = hashed_key * 21

        hashed_key = primed % self.size
        return hashed_key


if __name__ == "__main__":
    table = Hashtable()
    print(table.hash("hello"))
