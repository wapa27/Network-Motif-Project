
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
    newMatch = [[], []]
    # make a copy of possMatch using a for loop initialization
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
        # print(newMatch)
        # print("append", myNode.id, myNode.adj_list)
        # print("hPrime1:")
        # hPrime.PrintGraph()

    # replace nodes in hPrime with mapping from newMatch[0]
    for n in range(len(hPrime.nodeList)):  # loop thru hPrime's nodeList
        check = hPrime.nodeList[n]
        for m in range(len(newMatch[1])):  # loop the newMatch[1] list
            # if node in hPrime has same ID as node in newMatch[1]
            if check.id == newMatch[1][m]:
                # change node id to mapped value from newMatch[0]
                check.id = newMatch[0][m]

        # print("hPrime2:")
        # hPrime.PrintGraph()
        for a in range(len(check.adj_list)):
            mapped = False

            for b in range(len(newMatch[1])):
                # print(check.id, check.adj_list)
                adjCheck = check.adj_list[a]

                if adjCheck == newMatch[1][b]:
                    check.adj_list[a] = newMatch[0][b]
                    mapped = True
            if mapped == False:
                check.adj_list[a] = "$"
                # check.adj_list.pop(a)
        for z in check.adj_list:
            if(z == "$"):
                check.adj_list.remove(z)

    # print("trying", newMatch)
    if (gCompat(G, hPrime)):
        return newMatch
    else:
        return None


def recursiveSearch(G, H, g, possMatch, IsomorphList):
    for n in g.adj_list:
        if n not in possMatch[0]:
            # print(" node", n)
            possAdd = compatible(G, H, n, possMatch)
            if (possAdd != None):
                if len(possAdd[1]) == len(H.nodeList):
                    IsomorphList.append(possAdd)
                    # print("completed possAdd")
                    # print completed isomorphism
                    # print("completed possAdd: ", possAdd)

                else:
                    recursiveSearch(G, H, G.FindNode(n), possAdd, IsomorphList)


def IsomorphicExtentions(G, H, g):
    IsomorphList = []  # number of found subgraphs from node g
    # print(current.id)
    # G:graph, H:motif, current: node object of int n, g,h[0]: suppose g and h[0] are compatible, IsomorphList: record completed maps
    toopy = [[g.id], [H.nodeList[0].id]]
    recursiveSearch(G, H, g, toopy, IsomorphList)
    return IsomorphList


def noRep(listy):
    print("WRE SERTING!")
    for f in listy:
        for s in listy:
            # print("++++++++++++++++")
            # print("  trying", f[0], s[0])
            if (s != f):
                listy.remove(s)

    # print
    # print("Here is our listy:", listy)
    return listy


def FindSubgraphInstances(G, H):
    Instances = 0  # Final number of subgraphs
    tList = []
    for g in G.nodeList:
        print("id", g.id)
        tList += IsomorphicExtentions(G, H, g)
    print(tList)
    tList = noRep(tList)
    print(tList)
    Instances += len(tList)
    # check for repetitions
    return Instances


def hamilton(G, size, pt, path=[]):
    if pt not in set(path):
        path.append(pt)
        if len(path) == size:
            return path
        for pt_next in pt.adj_list:
            woo = G.FindNode(pt_next)
            res_path = [i for i in path]
            candidate = hamilton(G, size, woo, res_path)
            if candidate is not None:  # skip loop or dead end
                return candidate
    # loop or dead end, None is implicitly returned


if __name__ == "__main__":
    graph = LoadGraph("gra.txt")
    subgraph = LoadGraph("mot.txt")
    H = sortByDegree(subgraph)
    # H.PrintGraph()
    pt = H.nodeList[len(H.nodeList)-1]
    path = []
    HHam = hamilton(subgraph, len(subgraph.nodeList), pt, path)
    H.nodeList = HHam
    # H.PrintGraph()
    G = sortByDegree(graph)

    print("Graph: ")
    G.PrintGraph()
    print("Motif: ")
    H.PrintGraph()
    print("The number of instances of the motif is: ")
    print(FindSubgraphInstances(G, H))