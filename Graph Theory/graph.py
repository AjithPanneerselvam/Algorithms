"""
Basic operations in Graph DS
"""

class Graph(object):

    def __init__(self,graph = None):
        self.graph = graph


    def vertices(self):
        # Returns vertices in the graph
        return self.graph.keys()


    def edges(self):
        # Return edges in the graph
        edges = []

        for vert in self.graph:
            for verti in self.graph[vert]:
                if {vert,verti} not in edges:
                    edges.append({vert,verti})
        return edges


    def add_vertex(self,verti):
        # A new vertex is added to the graph
        if verti not in self.graph:
            self.graph[verti] = []


    def add_edge(self,edge):
        # An edge is added
        vertices = set(edge)
        vertex1,vertex2 = tuple(vertices)

        if vertex1 not in self.graph:
            self.graph[vertex1] = [vertex2]
        else:
            self.graph[vertex1].append(vertex2)

        if vertex2 not in self.graph:
            self.graph[vertex2] = [vertex1]

## Sample testcases ##
# graph = {
#     "a":["d"],
#     "b":["c"],
#     "c":["b","c","d","e"],
#     "d":["a"],
#     "e":["c"],
#     "f":[]
# }
#
# graph_obj = Graph(graph)
#
#
# print("Vertices of graph:")
# print(graph_obj.vertices())
#
# print("Edges of graph:")
# print(graph_obj.edges())
#
# print("Add vertex:")
# graph_obj.add_vertex("z")
#
# print("Vertices of graph:")
# print(graph_obj.vertices())
#
# print("Add an edge:")
# graph_obj.add_edge({"a","z"})
#
# print("Vertices of graph:")
# print(graph_obj.vertices())
#
# print("Edges of graph:")
# print(graph_obj.edges())
#
# print('Adding an edge {"x","y"} with new vertices:')
# graph_obj.add_edge({"x","y"})
# print("Vertices of graph:")
# print(graph_obj.vertices())
# print("Edges of graph:")
# print(graph_obj.edges())
