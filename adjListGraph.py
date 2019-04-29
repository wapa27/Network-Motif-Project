# Good to go
import sys
# from subgraphInstances import *


def FindSubgraphInstances(G, H):
    instances = []

    # sortByDegree(G)
    sortByDegree(H)


# def findAutomorphisms(H):


def sortByDegree(graph):
    for node in graph.nodeList:
        node.degree = len(node.adj_list)
    G_clone = sorted(graph.nodeList, key=lambda x: x.degree, reverse=True)
    for node in G_clone:
        print(node.id, node.adj_list, node.degree)


class Node:
    def __init__(self, id, adj_list, degree):
        self.id = id
        self.adj_list = adj_list
        self.degree = 0

    def AddAdj(self, connection):
        isConnected = self.FindAdj(connection)
        if(isConnected == False):  # if adjacent node not already in adj list
            self.adj_list.append(connection)		# add it to the adj list

    def FindAdj(self, connectFind):  # check adj list for adj node
        for connection in self.adj_list:
            if connection == connectFind:
                return True
        return False


class Graph:
    def __init__(self, nodeList):
        self.nodeList = nodeList

    def AddNode(self, node):
        nodeFind = self.FindNode(node)
        if(nodeFind == None):  # if node not already in graph
            nodeNew = Node(node, [], 0)  # create the node
            self.nodeList.append(nodeNew)  # add the node to graph
            return nodeNew
        return nodeFind

    def FindNode(self, query):  # determine if node already in graph
        for node in self.nodeList:
            if node.id == query:
                return node
        return None

    def PrintGraph(self):
        for node in self.nodeList:
            output = "" + node.id + " : "
            for connection in node.adj_list:
                output += connection + " -> "
            print(output)
    # def RemoveNode(self, query):
        # find query node
        # go thorugh node adjList to find nodes to detatch
        # remoce query node from graph

    def swapNodes(self, H, node1, node2):
        temp = node1.copy()
        node1.id = node2.id
        node2.id = temp.id


def LoadGraph(fileName):
    graph = Graph([])  # build graph
    with open(fileName) as f:
        f.readline()  # read past first two lines
        f.readline()
        for line in f:
            left, right = line.split()
            leftNode = graph.AddNode(left)
            leftNode.AddAdj(right)
            rightNode = graph.AddNode(right)
            rightNode.AddAdj(left)
    # graph.PrintGraph()
    return graph
    # if(graph.FindNode(left) != None):


graph = LoadGraph(sys.argv[1])
# print(len(graph.nodeList))
subgraph = LoadGraph(sys.argv[2])
FindSubgraphInstances(graph, subgraph)
