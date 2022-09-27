# Graph

Implementation of `Graph` data structure

## Challenge

Implement your own Graph. The graph should be represented as an adjacency list

## Approach & Efficiency

Node based approach

## Methods

- `add_node`
Arguments: value
Returns: The added node
Add a node to the graph
- `add_edge`
Arguments: 2 nodes to be connected by the edge, weight (optional)
Returns: nothing
Adds a new edge between two nodes in the graph
If specified, assign a weight to the edge
Both nodes should already be in the Graph
- `get_nodes`
Arguments: none
Returns all of the nodes in the graph as a collection (set, list, or similar)
- `get_neighbors`
Arguments: node
Returns a collection of edges connected to the given node
Include the weight of the connection in the returned collection
- `size`
Arguments: none
Returns the total number of nodes in the graph

- `depth_first_search`
Arguments: Vertex
Returns: A collection of nodes in their pre-order depth-first traversal order

Code Challenge 38 whiteboard:

![Whiteboard screenshot challenge 38](https://github.com/S14mx/data-structures-and-algorithms/blob/main/python/data_structures/graph/imgs/graph-dfs.png "Whiteboard process")

- [*Link to code*](./graph.py)
