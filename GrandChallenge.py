# Code by : Warren Payne, Liz Willie Chew
from adjListGraph import *


def gCompat(G, hPrime): # find out if the adj list of hPrime matches with 
    for n in hPrime.nodeList:
        for a in n.adj_list:
            lst = G.FindNode(n.id).adj_list
            if (a not in lst):
                return False
    return True


def compatible(G, H, toTry, possMatch):
    hPrime = Graph([])
    newMatch = [[], []]
    # make a copy of possMatch using a for loop initialization
    for i in range(len(possMatch[0])):
        newMatch[0].append(possMatch[0][i])
        newMatch[1].append(possMatch[1][i])
    # append the new node that we want to find compatibility
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

    # replace nodes in hPrime with mapping from newMatch[0]
    for n in range(len(hPrime.nodeList)):  # loop thru hPrime's nodeList
        check = hPrime.nodeList[n]
        for m in range(len(newMatch[1])):  # loop the newMatch[1] list
            # if node in hPrime has same ID as node in newMatch[1]
            if check.id == newMatch[1][m]:
                # change node id to mapped value from newMatch[0]
                check.id = newMatch[0][m]

        # loop through the adj list of the check node
        for a in range(len(check.adj_list)):
            mapped = False
            for b in range(len(newMatch[1])):
                adjCheck = check.adj_list[a]
                # if a match is found, replace the hPrime representation with the map
                if adjCheck == newMatch[1][b]:
                    check.adj_list[a] = newMatch[0][b]
                    mapped = True
            # mark non maps with a '$'
            if mapped == False:
                check.adj_list[a] = "$"
        # remove marked entries
        for z in check.adj_list:
            if(z == "$"):
                check.adj_list.remove(z)

    # find out if the mapped hPrime is a subset of G
    # if so, the hPrime is a match
    if (gCompat(G, hPrime)):
        return newMatch
    else:
        return None


def recursiveSearch(G, H, g, possMatch, IsomorphList):
    for n in g.adj_list:
        if n not in possMatch[0]:
            possAdd = compatible(G, H, n, possMatch)
            if (possAdd != None):
                if len(possAdd[1]) == len(H.nodeList):
                    IsomorphList.append(possAdd)
                else:
                    recursiveSearch(G, H, G.FindNode(n), possAdd, IsomorphList)


def IsomorphicExtentions(G, H, g):
    IsomorphList = []  # number of found subgraphs from node g
    toopy = [[g.id], [H.nodeList[0].id]] # inital mapping
    recursiveSearch(G, H, g, toopy, IsomorphList)
    return IsomorphList

def FindSubgraphInstances(G, H):
    Instances = 0  # Final number of subgraphs
    tList = []
    # call isomorphic extentions on all nodes in G
    for g in G.nodeList:
        tList += IsomorphicExtentions(G, H, g)
    tList = noRep(tList)
    Instances += len(tList)
    # check for repetitions
    return Instances


def noRep(listy):
    for f in listy:
        for s in listy:
            if (s != f):
                tmpf = []
                tmps = [] 
                for i in range(len(f[0])):
                	tmpf.append(f[0][i])
                	tmps.append(s[0][i])
                x = len(f) // 2
                x = int(x)
                y = x - 1
                if (sorted(tmpf) == sorted(tmps)):
                    if (len(f[0]) % 2 != 0):
                        if f[0][x] == s[0][x]:
                            listy.remove(s)
                    else:
                        if (f[0][x] == s[0][y]) and (f[0][y] == s[0][x]):
                            listy.remove(s)
    return listy


def hamilton(G, size, pt, path=[]):
    if pt not in set(path):
        path.append(pt)
        if len(path) == size:
            return path
        for pt_next in pt.adj_list:
            woo = G.FindNode(pt_next)
            res_path = [i for i in path]
            candidate = hamilton(G, size, woo, res_path)
            if candidate is not None: 
                return candidate
    # do not retrun anything if a hamiltonian path is not found


if __name__ == "__main__":
    graph = LoadGraph("graoh.txt")
    subgraph = LoadGraph("motif.txt")

    # order H by a Hamiltonian path 
    H = sortByDegree(subgraph)
    pt = H.nodeList[len(H.nodeList)-1]
    path = []
    HHam = hamilton(subgraph, len(subgraph.nodeList), pt, path)
    H.nodeList = HHam

    # sort G by the degrees of the nodes
    G = sortByDegree(graph)

    print("Graph: ")
    G.PrintGraph()
    print("Motif: ")
    H.PrintGraph()
    print("The number of instances of the motif is: ")
    print(FindSubgraphInstances(G, H))