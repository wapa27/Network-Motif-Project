from adjListGraph import *


#def compatible(G, H, toTry, possMatch):


def recursiveSearch(G,H,g,possMatch,IsomorphList):
	for n in g.adj_List:
		possAdd = compatible(G, H, n, possMatch)
		if (possAdd != None):
			if len(possAdd) == len(H.nodeList):
				IsomorphList.append(possAdd) #?
				return 1 #?
			else:
				recursiveSearch(G,H, n, possAdd, IsomorphList)
	return 0






def IsomorphicExtentions(G,H,g,possMatch):
	IsomorphList = [] # number of found subgraphs from node g
	for n in g.adj_list:
		print(type(n))
		current = G.FindNode(n)
		print(current.id)
		#G:graph, H:motif, current: node object of int n, g,h[0]: suppose g and h[0] are compatible, IsomorphList: record completed maps
		recursiveSearch(G,H,current,g,[g,h[0]],IsomorphList)
	return IsomorphList

def FindSubgraphInstances(G,H):
	Instances = 0 # Final number of subgraphs
	for g in G.nodeList:
		possMatch =[] ### do we need this?
		Instances += len(IsomorphicExtentions(G,H,g,possMatch))
		# remove g
		#check for repetitions?
	return Instances 


if __name__ == "__main__":
	graph = LoadGraph("eznetwork.txt")
	# print(len(graph.nodeList))
	subgraph = LoadGraph("ezmotif.txt")
	G = sortByDegree(graph)
	H = sortByDegree(subgraph)
	
	FindSubgraphInstances(G,H)


