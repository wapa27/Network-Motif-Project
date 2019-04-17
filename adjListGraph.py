# Good to go
import sys


class Node:
    def __init__(self, id, adj_list):
        self.id = id
        self.adj_list = adj_list

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
            nodeNew = Node(node, [])  # create the node
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
print(len(graph.nodeList))
