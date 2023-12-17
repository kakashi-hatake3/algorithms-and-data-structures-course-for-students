from graph import Graph, kruskal


def print_result(result, total_weight):
    for edge in result:
        edge_labels = [chr(ord('A') + idx) for idx in edge]
        edge_str = ' '.join(edge_labels)
        print(edge_str)
    print(total_weight)


with open("input.txt", 'r') as file:
    lines = file.readlines()

vertices = len(lines[0].split())
graph = Graph(vertices)

for i in range(1, vertices + 1):
    values = list(map(int, lines[i].split()))
    for j in range(vertices):
        graph.add_edge(i - 1, j, values[j])

result, total_weight = kruskal(graph)
print_result(result, total_weight)
