# Stacks and Queues

Classes for Stack and Queue data structures

## Challenge

Build a node based Stack and Queue classes

## Approach & Efficiency

All operations on Stack and Queue have O(1) complexity.

## API

Stack class has the following methods:

* `push`

Arguments: value
adds a new node with that value to the top of the stack with an O(1) Time performance.

* `pop`

Arguments: none
Returns: the value from node from the top of the stack
Removes the node from the top of the stack
Should raise exception when called on empty stack

* `peek`

Arguments: none
Returns: Value of the node located at the top of the stack
Should raise exception when called on empty stack

* `is_empty`

Arguments: none
Returns: Boolean indicating whether or not the stack is empty.

Queue class has the following methods:

* `enqueue`

Arguments: value
adds a new node with that value to the back of the queue with an O(1) Time performance.

* `dequeue`

Arguments: none
Returns: the value from node from the front of the queue
Removes the node from the front of the queue  
Should raise exception when called on empty queue

* `peek`

Arguments: none
Returns: Value of the node located at the front of the queue
Should raise exception when called on empty queue

* `is_empty`

Arguments: none
Returns: Boolean indicating whether or not the queue is empty
