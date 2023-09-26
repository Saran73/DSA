def add_node(v):
    if v in graph:
        print(v,"Node already exist")
    else:
        graph[v] = []

def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,"NOT FOUND")
    elif v2 not in graph:
        print(v2,"NOT FOUND")
    else:
        list1 = [v2,cost]
        list2 = [v1,cost]
        graph[v1].append(v2)
        graph[v2].append(list2)

def delete_node(v):
    if v not in graph:
        print(v,"NOT FOUND")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            for j in list1:
                if v==j[0]:
                    list1.remove(j)
                    break
            # if v in list1:
            #     list1.remove(v)




graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_edge("A","B",10)
add_edge("A","C",20)
add_edge("C","B",30)
add_edge("D","A",40)
add_edge("B","C",50)
delete_node("B")
print(graph)