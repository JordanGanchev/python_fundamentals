from collections import deque

nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(edges + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
end_node = int(input())

visited = [False] * (nodes + 1)
parent = [None] * (nodes + 1)

visited[start_node] = True
queue = deque([start_node])

while queue:
    node = queue.popleft()
    if node == end_node:
        break
    for child in graph[node]:
        if visited[child]:
            continue