from data_structures.stack_and_queue.stack import Stack


def multi_bracket_validation(str):
    stack = Stack()
    bracket_dict = {
        '{': '}',
        '(': ')',
        '[': ']'
    }

    for letter in str:
        if stack.is_empty() and letter in bracket_dict.values():
            return False
        if letter in bracket_dict.keys():
            stack.push(letter)
        if letter in bracket_dict.values() and letter == bracket_dict[stack.peek()]:
            stack.pop()

    return stack.is_empty()
