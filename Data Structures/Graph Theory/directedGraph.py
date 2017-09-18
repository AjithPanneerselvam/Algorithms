"""
Implementation of Directed Graph
"""


class Vertex:
    def __init__(self, label):
        self.label = str(label)
        self.adjList = {}

    def addNeighbour(self, toVertex, cost = 0):
        self.adjList[toVertex] = cost

    def getConnections(self):
        return self.adjList.keys()

    def getcost(self, toVertex):
        return self.adjList[toVertex]

    def getLabel(self):
        return self.label

    def __str__(self):
        return self.label + " connected to " + str([x.label for x in self.adjList])


class Graph:
    def __init__(self):
        self.verticesList = {}
        self.numVertices = 0

    def addVertex(self, label):
        self.numVertices += 1
        newVertex = Vertex(label)
        self.verticesList[label] = newVertex
        return newVertex

    def addEdge(self, fromVertex, toVertex, cost = 0):
        if fromVertex not in self.verticesList:
            startNewVertex = self.addVertex(fromVertex)
        if toVertex not in self.verticesList:
            endNewVertex = self.addVertex(toVertex)
        self.verticesList[fromVertex].addNeighbour(toVertex, cost)

    def getVertices(self):
        return self.verticesList.keys()

    def verticesCount(self):
        return self.numVertices

    def displayGraph(self):
        for vertex in self.verticesList:
            print (self.verticesList[vertex])



# Testcases - Directed Graph
def directedTestcases():
    g = Graph()

    for i in range(6):
        g.addVertex(chr(ord('A') + i))

    g.addEdge('A','B',2)
    g.addEdge('A','C',1)
    g.addEdge('A','F',2)
    g.addEdge('B','C',3)
    g.addEdge('D','A',1)
    g.addEdge('D','C',4)
    g.addEdge('D','E',5)

    # print (g.getVertices())
    # print (g.verticesCount())
    # g.displayGraph()

    return g
