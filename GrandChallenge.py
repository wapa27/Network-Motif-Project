from adjListGraph import *


def compatible(G, H, toTry, possMatch):
	hPrime = Graph([])
	newMatch = possMatch
	newMatch[0].append(toTry) # toTry is a string of node ID
	#print(len(newMatch)-1)
	#if (len(newMatch[1])>1):
	newMatch[1].append(H.nodeList[len(newMatch[0])-1]) #len(possMatch)-1 is index of h
	for i in range(len(newMatch[1])): #index of node IDs in G
		hPrime.nodeList.append(newMatch[1][i])
	hPrime.PrintGraph()
	print("---")
	# for i in range(len(hPrime.nodeList)):
	# 	hPrime.nodeList[i].id = newMatch[0][i].id
	# 	print("here")
	# 	print(hPrime.nodeList[i].id)
	#print("----")
	#print(newMatch[0])
	#for n in hPrime:




def recursiveSearch(G,H,g,possMatch,IsomorphList):
	print("g.id =" + g.id)
	#print(g.id + "adj_list is " + g.adj_list)
	for n in g.adj_list:
		print("node =" + n)
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
	toopy = ([g],[H.nodeList[0]])
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
	FindSubgraphInstances(G,H)


