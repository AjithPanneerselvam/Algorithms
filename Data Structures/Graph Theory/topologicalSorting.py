"""
Topological Sorting

Time-Complexity - O(V + E), where n is the number
Space-Complexity - O(V)
"""
from directedGraph import testcases


def topSortAux(g, vertex, visited, topSorted):
    visited.add(vertex)
    for child in g.verticesList[vertex].getConnections():
        if child not in visited:
            topSortAux(g, child, visited, topSorted)
    topSorted.append(vertex)


def topSort(g):
    visited = set()
    # topSorted uses stack ADT
    topSorted = list()
    for vertex in g.getVertices():
        if vertex not in visited:
            topSortAux(g, vertex, visited, topSorted)
    return topSorted


                              ### Testcases ###
g = testcases()
topSorted = topSort(g)
while(len(topSorted)):
    print(topSorted.pop())
