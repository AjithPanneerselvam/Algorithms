"""
Topological Sorting
"""
import graph


def travChildren(vertex,adj_graph,visited,topSorted):

    visited.add(vertex)
    for child in adj_graph[vertex]:
        if child in visited:
            continue

        travChildren(child,adj_graph,visited,topSorted)

    topSorted.append(vertex)


def topSort(adj_graph):
    visited = set()
    # topSorted is used as Stack ADT
    topSorted = list()

    for vertex in adj_graph:
        if vertex in visited:
            continue

        travChildren(vertex,adj_graph,visited,topSorted)

    return topSorted



                                ### Sample testcases ###
#
# graph_obj = graph.dirSampleTestcases()
# topSorted = topSort(graph_obj.graph)
# print (topSorted[::-1])
