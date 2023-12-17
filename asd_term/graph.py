from arrayList import ArrayList
from timsort import tim_sort


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = ArrayList()

        for i in range(vertices):
            temp_list = ArrayList()
            for i in range(vertices):
                temp_list.add(0)
            self.graph.add(temp_list)

    def add_edge(self, u, v, w):
        u_edge_array = self.graph.get(u)
        u_edge_array.set(v, w)
        v_edge_array = self.graph.get(v)
        v_edge_array.set(u, w)


def find_e(parent, i):
    if parent[i] == i:
        return i
    return find_e(parent, parent[i])


def union_sets(parent, rank, x, y):
    root_x = find_e(parent, x)
    root_y = find_e(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def kruskal(graph):
    edges = ArrayList()
    for i in range(graph.V):
        for j in range(i + 1, graph.V):
            if graph.graph.get(i).get(j) != 0:
                edges.add((graph.graph.get(i).get(j), i, j))
    edges = tim_sort(edges)
    parent = [i for i in range(graph.V)]
    rank = [0] * graph.V
    result = ArrayList()
    total_weight = 0
    for edge in edges:
        weight, u, v = edge
        root_u = find_e(parent, u)
        root_v = find_e(parent, v)
        if root_u != root_v:
            result.add((u, v))
            total_weight += weight
            union_sets(parent, rank, root_u, root_v)
    return result, total_weight
