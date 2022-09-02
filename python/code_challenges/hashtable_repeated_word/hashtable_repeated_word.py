from data_structures.hash_table.hashtable import Hashtable


def first_repeated_word(string):
    hash_table = Hashtable()
    words = string.lower().split()
    # alpha_words = []
    # for word in words:
    #     alpha_word = ""

    #     for letter in word:
    #         if letter.isalpha():
    #             alpha_word += letter
    #     alpha_words.append(alpha_word)
    alpha_words = (["".join([letter for letter in word if letter.isalpha()])
                    for word in words])

    for word in alpha_words:

        if hash_table.contains(word):
            return word or None
        else:
            hash_table.set(word, True)
