from adjListGraph import *


def compatible(G, H, toTry, possMatch):
	hPrime = Graph([])
	newMatch = [[],[]]
	for i in range(len(possMatch[0])):
		newMatch[0].append(possMatch[0][i])
		newMatch[1].append(possMatch[1][i])
	newMatch[0].append(toTry)
	newMatch[1].append(H.nodeList[len(newMatch[0])-1].id) #len(possMatch)-1 is index of h
	print(newMatch[1])
	print(newMatch[0])
	
	for i in range(len(newMatch[1])): #index of node IDs in G
		hPrime.nodeList.append(H.nodeList[i])
	hPrime.PrintGraph()

def recursiveSearch(G,H,g,possMatch,IsomorphList):
	print("g.id = " + g.id)
	for n in g.adj_list:
		print("node = " + n)
		possAdd = compatible(G, H, n, possMatch)
		if (possAdd != None):
			if len(possAdd) == len(H.nodeList):
				IsomorphList.append(possAdd) #?
				return 1 #?
			else:
				recursiveSearch(G,H, n, possAdd, IsomorphList)
	return 0

def IsomorphicExtentions(G,H,g):
	IsomorphList = [] # number of found subgraphs from node g
		#print(current.id)
		#G:graph, H:motif, current: node object of int n, g,h[0]: suppose g and h[0] are compatible, IsomorphList: record completed maps
	toopy = [[g.id],[H.nodeList[0].id]]
	hold = recursiveSearch(G,H,g,toopy,IsomorphList)
	return IsomorphList

'''
def IsomorphicExtentions(G,H,g,possMatch):
	IsomorphList = [] # number of found subgraphs from node g
	for n in g.adj_list:
		current = G.FindNode(n)
		#print(current.id)
		#G:graph, H:motif, current: node object of int n, g,h[0]: suppose g and h[0] are compatible, IsomorphList: record completed maps
		toopy = ([g],[H.nodeList[0]])
		hold = recursiveSearch(G,H,current,toopy,IsomorphList)
	return IsomorphList
'''

def FindSubgraphInstances(G,H):
	Instances = 0 # Final number of subgraphs
	for g in G.nodeList:
		possMatch = [] ### do we need this?
		Instances += len(IsomorphicExtentions(G,H,g))
		#check for repetitions ?
	return Instances 


if __name__ == "__main__":
	graph = LoadGraph("eznetwork.txt")
	# print(len(graph.nodeList))
	subgraph = LoadGraph("ezmotif.txt")
	G = sortByDegree(graph)
	H = sortByDegree(subgraph)
	
	G.PrintGraph()
	H.PrintGraph()
	print("--------")
	FindSubgraphInstances(G,H)


