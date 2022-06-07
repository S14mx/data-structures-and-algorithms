# Singly Linked List

Implementation of `linked list` data structure

## Challenge

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node
Create a Linked List class
Within your Linked List class, include a head property.
Upon instantiation, an empty Linked List should be created.

## Approach & Efficiency

Node based approach

## Methods

`insert`
Arguments: value
Returns: nothing
Adds a new node with that value to the head of the list with an O(1) Time performance.
`includes`
Arguments: value
Returns: Boolean
Indicates whether that value exists as a Node’s value somewhere within the list.
`to string`
Arguments: none
Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"
`append`
Arguments: new value
Returns: nothing
Adds a new node with the given value to the end of the list
`insert before`
Arguments: value, new value
Returns: nothing
Adds a new node with the given new value immediately before the first node that has the value specified
`insert after`
Arguments: value, new value
Returns: nothing
Adds a new node with the given new value immediately after the first node that has the value specified

![Whiteboard screenshot](https://github.com/S14mx/data-structures-and-algorithms/blob/main/python/data_structures/linked_list/imgs/linked_list_insertions.png "Whiteboard process")

- [*Link to code*](./linked_list.py)
