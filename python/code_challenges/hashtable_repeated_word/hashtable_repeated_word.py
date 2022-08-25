from data_structures.hash_table.hashtable import Hashtable


def first_repeated_word(string):
    hash_table = Hashtable()
    words = string.split()
    for word in words:

        if hash_table.contains(word.lower()):
            return word or None
        else:
            hash_table.set(word.lower(), True)


if __name__ == "__main__":
    print(first_repeated_word("hello there hello"))
