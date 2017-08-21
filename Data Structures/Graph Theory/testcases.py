"""
Testcases
"""
from graph import Graph


def undirSampleTestcases():
    graphObj = Graph()
    graphObj.undirAddEdge(['a','b'])
    graphObj.undirAddEdge(['a','d'])
    graphObj.undirAddEdge(['b','c'])
    graphObj.undirAddEdge(['b','f'])
    graphObj.undirAddEdge(['c','f'])
    graphObj.undirAddEdge(['c','g'])
    graphObj.undirAddEdge(['d','e'])
    graphObj.undirAddEdge(['e','g'])
    return graphObj


def weightedUndirSampleTestcases():
    graphObj = Graph()
    graphObj.undirAddEdgeWeight(['a','b'], 2)
    graphObj.undirAddEdgeWeight(['a','d'], 1)
    graphObj.undirAddEdgeWeight(['b','c'], 1)
    graphObj.undirAddEdgeWeight(['b','d'], 4)
    graphObj.undirAddEdgeWeight(['c','d'], 2)
    graphObj.undirAddEdgeWeight(['c','g'], 3)
    graphObj.undirAddEdgeWeight(['d','g'], 2)
    return graphObj


def dirSampleTestcases():
    graphObj = Graph()
    graphObj.dirAddEdge(['a','b'])
    graphObj.dirAddEdge(['b','c'])
    graphObj.dirAddEdge(['c','g'])
    graphObj.dirAddEdge(['b','f'])
    graphObj.dirAddEdge(['c','f'])
    graphObj.dirAddEdge(['a','d'])
    graphObj.dirAddEdge(['d','e'])
    graphObj.dirAddEdge(['e','g'])
    return graphObj


def weightedDirSampleTestcases():
    graphObj = Graph()
    graphObj.dirAddEdgeWeight(['a','b'], 2)
    graphObj.dirAddEdgeWeight(['a','d'], 3)
    graphObj.dirAddEdgeWeight(['b','d'], 4)
    graphObj.dirAddEdgeWeight(['b','c'], 1)
    graphObj.dirAddEdgeWeight(['d','e'], 3)
    graphObj.dirAddEdgeWeight(['c','f'], 3)
    graphObj.dirAddEdgeWeight(['e','c'], 1)
    graphObj.dirAddEdgeWeight(['e','f'], 1)
    return graphObj


#                                         ### Sample testcases ###
#
# undirGraphObj = undirSampleTestcases()
# print (undirGraphObj.vertices(), undirGraphObj.edges())
# print ("Undirected Graph" , undirGraphObj.graph)
#
# dirGraphObj = dirSampleTestcases()
# print (dirGraphObj.vertices(), dirGraphObj.edges())
# print ("Directed Graph" , dirGraphObj.graph)
