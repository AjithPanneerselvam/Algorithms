"""
Implementation of Graph Data Structure
"""

class Graph(object):

    def __init__(self,graph = None):
        self.graph = graph


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
    def undirAddEdge(self,edge):
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


    # Add edge in a directed graph
    def dirAddEdge(self,edge):
        # vertex1 -> vertex2
        vertex1, vertex2 = edge[0], edge[1]
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

        if vertex2 not in self.graph:
            self.graph[vertex2] = []


def undirSampleTestcases():

    graph_obj = Graph({})

    graph_obj.undirAddEdge(['a','b'])
    graph_obj.undirAddEdge(['a','d'])
    graph_obj.undirAddEdge(['b','c'])
    graph_obj.undirAddEdge(['b','f'])
    graph_obj.undirAddEdge(['c','f'])
    graph_obj.undirAddEdge(['c','g'])
    graph_obj.undirAddEdge(['d','e'])
    graph_obj.undirAddEdge(['e','g'])

    return graph_obj


def dirSampleTestcases():

    graph_obj = Graph({})

    graph_obj.dirAddEdge(['a','b'])
    graph_obj.dirAddEdge(['b','c'])
    graph_obj.dirAddEdge(['c','g'])
    graph_obj.dirAddEdge(['b','f'])
    graph_obj.dirAddEdge(['c','f'])
    graph_obj.dirAddEdge(['a','d'])
    graph_obj.dirAddEdge(['d','e'])
    graph_obj.dirAddEdge(['e','g'])

    return graph_obj


#                                         ### Sample testcases ###
#
# undir_graph_obj = undirSampleTestcases()
# print undir_graph_obj.vertices(), undir_graph_obj.edges()
# print "Undirected Graph" , undir_graph_obj.graph
#
# dir_graph_obj = dirSampleTestcases()
# print dir_graph_obj.vertices(), dir_graph_obj.edges()
# print "Directed Graph" , dir_graph_obj.graph
