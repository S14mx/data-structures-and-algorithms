from python.data_structures.hash_table.hashtable import Hashtable


def first_repeated_word(string):
    hash_table = Hashtable
    words = string.split()
    for word in words:
        hash_table.set(word, True)
        if hash_table.contains(word):
            return word or None


if __name__ == "__main__":
    print(first_repeated_word("hello there"))
