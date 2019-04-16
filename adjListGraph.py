# naive read-in. Need to clean this up. Just wanted to get something together.
# let's put the read-in into a function, and we need to take .net file as input arg.


class Node:
    def __init__(self, id, adj_list):
        self.id = id
        self.adj_list = adj_list

    def AddAdj(self, connection):
    	isConnected = self.FindAdj(connection)
    	if(isConnected == False):
    		self.adj_list.append(connection)

    def FindAdj(self, connectFind):
		for connection in self.adj_list:
			if connection == connectFind:
				return True
		return False

class Graph:
	def __init__(self, nodeList):
		self.nodeList = nodeList

	def AddNode(self, node):
		nodeFind = self.FindNode(node)
		if(nodeFind == None):
			nodeNew = Node(node, [])
			self.nodeList.append(nodeNew)
			return nodeNew
		return nodeFind

	def FindNode(self, query):
		for node in self.nodeList:
			if node.id == query:
				return node
		return None

	def PrintGraph(self):
		for node in self.nodeList:
			output = "" + node.id + " : "
			for connection in node.adj_list:
				output += connection + " -> "
			print output
	#def RemoveNode(self, query):
		# find query node
		# go thorugh node adjList to find nodes to detatch
		# remoce query node from graph

def LoadGraph(fileName):
	graph = Graph([])
	with open(fileName) as f:
		f.readline() # read past first two lines
		f.readline()
		for line in f:
			left, right = line.split()
			leftNode = graph.AddNode(left)
			leftNode.AddAdj(right)
			rightNode = graph.AddNode(right)
			rightNode.AddAdj(left)
	graph.PrintGraph()
	return graph
			#if(graph.FindNode(left) != None):

graph = LoadGraph('graph1.net')