class Graph:
    """
    Graph data structure class
    """

    def __init__(self):
        self.adj_list = []

    def __str__(self):

        return [vertex.value for vertex in self.adj_list]

    def size(self):
        """
        Arguments:
            none

        Returns:
            Total number of vertices in the graph
        """

        return len(self.adj_list)

    def add_node(self, value):
        """
        Adds a node to the graph

        Arguments:
            value

        Returns:
            The added node
        """
        new_vertex = Vertex(value)
        self.adj_list.append(new_vertex)

        return new_vertex

    def add_edge(self, start, vertex, weight=0):
        """Adds a new edge between two nodes in the graph. Both nodes should already be in the Graph

        Args:
            start (Vertex): connection from
            vertex (Vertex): connection to
            weight (int, optional): Defaults to 0.

        Raises:
            KeyError: if either of the nodes is not in the graph
        """
        if start in self.adj_list and vertex in self.adj_list:
            new_edge = Edge(vertex, weight)
            for node in self.adj_list:
                if node == start:
                    node.neighbors.append(new_edge)
        else:
            raise KeyError

    def get_nodes(self):
        """Returns all of the nodes in the graph as a collection

        Returns:
            list of Vertex instances
        """

        return self.adj_list

    def get_neighbors(self, vertex):
        """Returns a collection of edges connected to the given node

        Args:
            vertex (Vertex): _description_

        Returns:
            list of Edge instances
        """
        for node in self.adj_list:
            if node == vertex:

                return node.neighbors

    def depth_first_search(self, node, visited=None):
        if visited is None:
            visited = []
        if node.value in visited:
            return
        if node in self.adj_list:
            visited.append(node.value)

        for neighbor in node.neighbors:
            if neighbor.vertex.value not in visited:
                self.depth_first_search(neighbor.vertex, visited)

        return visited


class Vertex:
    """Vertex(node) class for Graph data structure
    """

    def __init__(self, value, neighbors=None):
        self.value = value
        self.neighbors = neighbors if neighbors else []

    def __str__(self):

        return f"{self.value}"


class Edge:
    """Edge class for Graph data structure
    """

    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    def __str__(self):

        return f"{self.vertex.value}"
