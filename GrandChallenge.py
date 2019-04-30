from adjListGraph import *

def recursiveSearch(G,H,h,tuple,IsomorphList):
	

def IsomorphicExtentions(G,H,g,possMatch):
	IsomorphList = [] # number of found subgraphs from node g
	for n in g.adj_list:
		current = G.findNode(n)
		#G:graph, H:motif, current: node object of int n, g,h[0]: suppose g and h[0] are compatible, IsomorphList: record completed maps
		recursiveSearch(G,H,current,h,[g,h[0]],IsomorphList)


def FindSubgraphInstances(G,H):
	Instances = 0 # Final number of subgraphs
	for g in G:
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


