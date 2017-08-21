"""
Implementation of Graph Data Structure
"""

class Graph(object):
    def __init__(self):
        self.graph = {}


    def vertices(self):
        # Return vertices in the graph
        return self.graph.keys()


    def edges(self):
        # Return edges in the graph
        edges = []
        for vert in self.graph:
            for verti in self.graph[vert]:
                if {vert,verti} not in edges:
                    edges.append({vert,verti})
        return edges


    # Add edge in an undirected graph
    def undirAddEdge(self, edge):
        # An edge is added
        vertices = set(edge)
        vertex1,vertex2 = tuple(vertices)
        if vertex1 not in self.graph:
            self.graph[vertex1] = [vertex2]
        else:
            self.graph[vertex1].append(vertex2)

        if vertex2 not in self.graph:
            self.graph[vertex2] = [vertex1]
        else:
            self.graph[vertex2].append(vertex1)


    # Add edge in an undirected graph along with edge weight
    def undirAddEdgeWeight(self, edge, weight):
        vertex1, vertex2 = edge[0], edge[1]
        if vertex1 not in self.graph:
            self.graph[vertex1] = [vertex2, weight]
        else:
            self.graph[vertex1].append([vertex2, weight])

        if vertex2 not in self.graph:
            self.graph[vertex2] = [vertex1, weight]
        else:
            self.graph[vertex2].append(vertex1, weight)


    # Add edge in a directed graph
    def dirAddEdge(self, edge):
        # vertex1 -> vertex2
        vertex1, vertex2 = edge[0], edge[1]
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

        if vertex2 not in self.graph:
            self.graph[vertex2] = []


    # Add edge in a directed graph along with edge weight
    def dirAddEdgeWeight(self, edge, weight):
        # vertex1 -> vertex2
        vertex1, vertex2 = edge[0], edge[1]
        if vertex1 in self.graph:
            self.graph[vertex1].append([vertex2, weight])
        else:
            self.graph[vertex1] = [vertex2, weight]

        if vertex2 not in self.graph:
            self.graph[vertex2] = []
