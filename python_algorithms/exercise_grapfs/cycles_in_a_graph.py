graph = {}

while True:
    line = input()
    if line == 'End':
        break
    source, destination = line.split('-')
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(destination)

print(graph)
