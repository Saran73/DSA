def add_node(v):
    global node_count
    if v in nodes:
        print(v,"Node is already present")
    else:
        node_count += 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(v1,"Not present in graph")
    elif v2 not in nodes:
        print(v2, "Not present in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        #graph[index2][index1] = cost

def delete_node(v):
    global node_count
    if v  not in nodes:
        print(v,"NOT FOUND")
    else:
        index1 = nodes.index(v)
        node_count -= 1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"NOT FOUND")
    elif v2 not in nodes:
        print(v2,"NOT FOUND")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0





def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"),end=" ")
        print()



nodes = []
graph = []
node_count = 0
# print("Before adding nodes")
# print(nodes)
# print(graph)
add_node("A")
add_node("B")
add_node("D")
add_edge("A","B",4)
add_edge("A","D",6)
print_graph()
delete_edge("A","C")
print("After Deleting")
print_graph()
print(nodes)
print(node_count)
