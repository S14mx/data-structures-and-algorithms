class Graph:
    """
    Graph data structure
    """

    def __init__(self):
        self.adj_list = []

    def __str__(self):
        return [vertex.value for vertex in self.adj_list]

    def size(self):
        return len(self.adj_list)

    def add_node(self, value):
        new_vertex = Vertex(value)
        self.adj_list.append(new_vertex)
        return new_vertex

    def add_edge(self, start, end, weight=0):
        new_edge = Edge(start, end, weight)
        pass

    def get_nodes(self):
        return self.adj_list


class Vertex:
    def __init__(self, value, neighbors=[]):
        self.value = value
        self.neighbors = neighbors

    def __str__(self):
        return f"{self.value}"


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self):
        return f"{self.end.value}"
