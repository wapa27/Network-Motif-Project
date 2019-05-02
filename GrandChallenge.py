from adjListGraph import *

def gCombat(G, hPrime):
	for n in hPrime.nodeList:
		for a in n.adj_list:
			lst = G.FindNode(n.id).adj_list
			if (a not in lst):
				return False
	return True

def compatible(G, H, toTry, possMatch):
	print("H: ")
	H.PrintGraph()
	hPrime = Graph([])
	myNode = Node(0, [], 0)
	newMatch = [[],[]]
	#make a copy of possMatch using a for loop initialization
	for i in range(len(possMatch[0])):
		newMatch[0].append(possMatch[0][i])
		newMatch[1].append(possMatch[1][i])
	newMatch[0].append(toTry)
	newMatch[1].append(H.nodeList[len(newMatch[0])-1].id) #len(possMatch)-1 is index of h
	#print(newMatch[1])
	#print(newMatch[0])
	#make a copy of H using a for loop initialization
	for i in range(len(newMatch[1])): #index of node IDs in G
		myNode.id = H.nodeList[i].id
		for x in H.nodeList[i].adj_list:
			if x != myNode.id:
				myNode.adj_list.append(x)
		hPrime.nodeList.append(myNode)
	print("hprime: ")
	hPrime.PrintGraph()
	#replace nodes in hPrime with mapping from newMatch[0]
	for n in range(len(hPrime.nodeList)): #loop thru hPrime's nodeList
		check = hPrime.nodeList[n]
		for m in range(len(newMatch[1])): #loop the newMatch[1] list
			if check.id == newMatch[1][m]: #if node in hPrime has same ID as node in newMatch[1]
				check.id = newMatch[0][m] #change node id to mapped value from newMatch[0]
		for a in range(len(check.adj_list)): #loop thru adj list to change values
			for b in range(len(newMatch[1])):
				adjCheck = check.adj_list[a]
				if adjCheck == newMatch[1][b]:
					check.adj_list[a] = newMatch[0][b]
	if (gCombat(G, hPrime)):
		return newMatch
	else:
		return None

def recursiveSearch(G,H,g,possMatch,IsomorphList):
	print("g.id = " + g.id)
	for n in g.adj_list:
		print("node = " + n)
		print("possMatch: ")
		print(possMatch)
		possAdd = compatible(G, H, n, possMatch)
		if (possAdd != None):
			if len(possAdd[1]) == len(H.nodeList):
				IsomorphList.append(possAdd) #?
				print("IsomorphList: ")
				print(IsomorphList)
				print("H: ")
				H.PrintGraph()
				return 1
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
def IsomorphicExtentions(G,H,g):
	IsomorphList = [] # number of found subgraphs from node g
	for n in g.adj_list:
		current = G.FindNode(n)
		#print(current.id)
		#G:graph, H:motif, current: node object of int n, g,h[0]: suppose g and h[0] are compatible, IsomorphList: record completed maps
		toopy = ([g.id],[H.nodeList[0].id])
		hold = recursiveSearch(G,H,g,toopy,IsomorphList)
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
	
	#G.PrintGraph()
	#H.PrintGraph()
	print("H: ")
	H.PrintGraph()
	print("--------")
	print(FindSubgraphInstances(G,H))
	H.PrintGraph()


