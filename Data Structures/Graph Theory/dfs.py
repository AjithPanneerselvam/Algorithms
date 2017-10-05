"""
Depth First Search

Time-Complexity - O(V + E)
Space-Complexity - O(V)
"""

from undirectedGraph import undirectedTestcases
from directedGraph import directedTestcases


def dfsTraversal(g, vertex, visited, dfsOrder):
    visited.add(vertex)
    dfsOrder.append(vertex)

    for vertex in g.verticesList[vertex].getConnections():
        if vertex not in visited:
            dfsTraversal(g, vertex, visited, dfsOrder)


def dfs(g, visited, dfsOrder):
    for vertex in g.getVertices():
        if vertex not in visited:
            dfsTraversal(g, vertex, visited, dfsOrder)
    return dfsOrder



#                                       ### Testcases ###
g = undirectedTestcases()
print(dfs(g, visited = set(), dfsOrder = list()))
g = directedTestcases()
print(dfs(g, visited = set(), dfsOrder = list()))
