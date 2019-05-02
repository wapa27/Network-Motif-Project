from adjListGraph import *

def gCompat(G, hPrime):
	for n in hPrime.nodeList:
		for a in n.adj_list:
			lst = G.FindNode(n.id).adj_list
			if (a not in lst):
				return False
	return True

def compatible(G, H, toTry, possMatch):
	hPrime = Graph([])
	newMatch = [[],[]]
	#make a copy of possMatch using a for loop initialization
	for i in range(len(possMatch[0])):
		newMatch[0].append(possMatch[0][i])
		newMatch[1].append(possMatch[1][i])
	newMatch[0].append(toTry)
	newMatch[1].append(H.nodeList[len(newMatch[0])-1].id)

	# populate hPrime
	for i in range(len(newMatch[1])): 
		myNode = Node(0, [], 0)
		myNode.id = H.nodeList[i].id
		for x in H.nodeList[i].adj_list:
			if x != myNode.id:
				myNode.adj_list.append(x)
		hPrime.nodeList.append(myNode)

	#replace nodes in hPrime with mapping from newMatch[0]
	for n in range(len(hPrime.nodeList)): #loop thru hPrime's nodeList
		check = hPrime.nodeList[n]
		for m in range(len(newMatch[1])): #loop the newMatch[1] list
			if check.id == newMatch[1][m]: #if node in hPrime has same ID as node in newMatch[1]
				check.id = newMatch[0][m] #change node id to mapped value from newMatch[0]
		'''
		for a in range(len(check.adj_list)): #loop thru adj list to change values
			for b in range(len(newMatch[1])):
				adjCheck = check.adj_list[a]
				if adjCheck == newMatch[1][b]:
					check.adj_list[a] = newMatch[0][b]
		'''
		for a in range(len(check.adj_list)): 
			mapped = False
			for b in range(len(newMatch[1])):
				adjCheck = check.adj_list[a]
				if adjCheck == newMatch[1][b]:
					check.adj_list[a] = newMatch[0][b]
					mapped = True
			if mapped == False:
				check.adj_list.pop(a)

	if (gCompat(G, hPrime)):
		return newMatch
	else:
		return None

def recursiveSearch(G,H,g,possMatch,IsomorphList):
	for n in g.adj_list:
		possAdd = compatible(G, H, n, possMatch)
		if (possAdd != None):
			if len(possAdd[1]) == len(H.nodeList):
				IsomorphList.append(possAdd)
				print(possAdd)
			else:
				recursiveSearch(G,H, G.FindNode(n), possAdd, IsomorphList)

def IsomorphicExtentions(G,H,g):
	IsomorphList = [] # number of found subgraphs from node g
		#print(current.id)
		#G:graph, H:motif, current: node object of int n, g,h[0]: suppose g and h[0] are compatible, IsomorphList: record completed maps
	toopy = [[g.id],[H.nodeList[0].id]]
	recursiveSearch(G,H,g,toopy,IsomorphList)
	return IsomorphList

def noRep(listy):
	for f in listy:
		for s in listy: 
			if (s != f):
				print(sorted(f[0]))
				print(sorted(s[0]))
				if (sorted(f[0]) == sorted(s[0])):
					listy.remove(f)
	return listy  



def FindSubgraphInstances(G,H):
	Instances = 0 # Final number of subgraphs
	tList = []
	for g in G.nodeList:
		tList += IsomorphicExtentions(G,H,g)
		tList = noRep(tList)
		print("tlist")
		print(tList)
	Instances += len(tList)
	#check for repetitions
	return Instances 


if __name__ == "__main__":
	graph = LoadGraph("eznetwork.txt")
	# print(len(graph.nodeList))
	subgraph = LoadGraph("ezmotif.txt")
	G = sortByDegree(graph)
	H = sortByDegree(subgraph)

	print("Graph: ")
	G.PrintGraph()
	print("Motif: ")
	H.PrintGraph()
	
	print(FindSubgraphInstances(G,H))