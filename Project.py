# naive read-in. Need to clean this up. Just wanted to get something together.
# let's put the read-in into a function, and we need to take .net file as input arg.
import sys


class node:
    def __init__(self, id, adj_list):
        self.id = id
        self.adj_list = adj_list

    def _str_(self):
        return id


def main():
    graph = []
    with open(sys.argv[1]) as f:  # open argument 2 (parent graph)
        blank_list = []  # if making new node, we need blank adj list
        for i in range(3):  # first two lines we don't want
            line = f.readline()
            if(i == 2):             # building our first two nodes / first connection
                root, adj = line.split()
                root = node(root, blank_list)
                adj = node(adj, blank_list)
                graph.append(root)
                graph.append(adj)
                adj.adj_list.append(graph[0])
                graph[0].adj_list.append(adj)
        for line in f:
            blank_list = []
            root_status = False         # root node NOT in graph
            adj_status = False          # adj node NOT in graph
            root, adj = line.split()
            for j in range(len(graph)):
                if root == graph[j].id:  # root already a node in graph
                    root_status = True
                    for k in range(len(graph)):  # check if adjacent node in graph too
                        if adj == graph[k].id:  # if adj node in graph already
                            adj_status = True
                            # append adj node to root node list
                            graph[k].adj_list.append(graph[j])
                            graph[j].adj_list.append(graph[k])
                            break
                    if adj_status == False:  # if adjacent node not already in graph
                        adj = node(adj, blank_list)
                        graph[j].adj_list.append(adj)
                        adj.adj_list.append(graph[j])
                        graph.append(adj)
            if root_status == False:  # root not in graph yet
                root = node(root, blank_list)
                graph.append(root)
                for k in range(len(graph)):  # check if adjacent node is in graph too
                    if adj == graph[k].id:  # if adj node in graph already
                        adj_status = True
                        # append adj node to root node list
                        graph[j].adj_list.append(graph[k])
                        graph[k].adj_list.append(graph[j])

                if adj_status == False:  # if adjacent node not already in graph
                    adj = node(adj, blank_list)
                    root.adj_list.append(adj)
                    adj.adj_list.append(root)
                    graph.append(adj)
    count = 0
    tmp = []
    # quick test (printing count of edges --> given at top of .net file)
    for x in range(0, len(graph)):
        if graph[x].id not in tmp:
            tmp.append(graph[x])
    print(len(graph))


main()
