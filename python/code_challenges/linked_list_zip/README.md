# Challenge Summary

Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped list.
My partner for this assignment was Aoife Mulligan

## Whiteboard Process

![Whiteboard screenshot](https://github.com/S14mx/data-structures-and-algorithms/blob/linked-list-zip/python/code_challenges/linked_list_zip/imgs/linked-list-zip.png "Whiteboard process")

## Approach & Efficiency

We decided to mutate first list in place so we don't have to create a new data structure and hinder space efficiency.
Time complexity for this solution is O(n)
Space complexity is O(1)

## Solution

To test our code, install `pytest` library an then run `pytest tests/code_challenges/test_linked_list_zip.py` from `python` directory.

- [*Link to code*](/python/code_challenges/linked_list_zip/linked_list_zip.py)
