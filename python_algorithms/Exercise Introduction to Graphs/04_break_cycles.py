def dfs(node, destination, graph, visited):
    if node in visited:
        return
    visited.add(node)
    if node == destination:
        return
    for child in graph[node]:
        dfs(child, destination, graph, visited)


def path_exists(source, destination, green):
    visited = set()

    dfs(source, destination, graph, visited)

    return destination in visited

from reportlab.lib.colors import green

nodes = int(input())

graph = {}
edges = []
for _ in range(nodes):
    node, children_str = input().split(' -> ')
    children = children_str.split()
    graph[node] = children
    for child in children:
        edges.append((node, child))

remove_edges = []

for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] and source not in graph[destination]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exists(source, destination, green):
        remove_edges.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f"Edges to remove: {len(remove_edges)}")
for first, second in remove_edges:
    print(f'{first} - {second}')