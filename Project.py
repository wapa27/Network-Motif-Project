# naive read-in. Need to clean this up. Just wanted to get something together.


class node:
    def __init__(self, id, adj_list):
        self.id = id
        self.adj_list = adj_list

    def _str_(self):
        return id


graph = []
with open('graph3.net') as f:
    blank_list = []
    for i in range(3):
        line = f.readline()
        if(i == 2):
            root, adj = line.split()
            root = node(root, blank_list)
            adj = node(adj, blank_list)
            graph.append(root)
            graph[0].adj_list.append(adj)
    for line in f:
        blank_list = []
        root_status = False         # root node NOT in graph
        adj_status = False          # adj node NOT in graph
        root, adj = line.split()
        for j in range(len(graph)-1):
            if root == graph[j].id:  # root already a node in graph
                root_status = True
                for k in range(len(graph)-1):  # check if adjacent node in graph too
                    if adj == graph[k].id:  # if adj node in graph already
                        adj_status = True
                        # append adj node to root node list
                        graph[j].adj_list.append(graph[k])
                        break
                if adj_status == False:  # if adjacent node not already in graph
                    adj = node(adj, blank_list)
                    graph[j].adj_list.append(adj)
                    graph.append(adj)
        if root_status == False:  # root not in graph yet
            root = node(root, blank_list)
            graph.append(root)
            for k in range(len(graph)-1):  # check if adjacent node is in graph too
                if adj == graph[k].id:  # if adj node in graph already
                    adj_status = True
                    # append adj node to root node list
                    graph[j].adj_list.append(graph[k])

            if adj_status == False:  # if adjacent node not already in graph
                adj = node(adj, blank_list)
                root.adj_list.append(adj)
                graph.append(adj)

print(graph[0].adj_list[0].id)  # should index 0 of first node's adj list
