# from collections import defaultdict
#
#
# def find_important_streets():
#     def dfs(node, parent, visited, disc, low, bridges, graph, time):
#         visited[node] = True
#         disc[node] = low[node] = time[0]
#         time[0] += 1
#
#         for neighbor in graph[node]:
#             if not visited[neighbor]:
#                 dfs(neighbor, node, visited, disc, low, bridges, graph, time)
#                 low[node] = min(low[node], low[neighbor])
#
#                 if low[neighbor] > disc[node]:
#                     bridges.append(tuple(sorted((node, neighbor))))
#             elif neighbor != parent:
#                 low[node] = min(low[node], disc[neighbor])
#
#     # Input reading
#     buildings = int(input())
#     streets = int(input())
#     graph = defaultdict(list)
#
#     for _ in range(streets):
#         a, b = map(int, input().split(' - '))
#         graph[a].append(b)
#         graph[b].append(a)
#
#     # Initialization
#     visited = [False] * buildings
#     disc = [-1] * buildings
#     low = [-1] * buildings
#     bridges = []
#     time = [0]
#
#     # Finding bridges
#     for i in range(buildings):
#         if not visited[i]:
#             dfs(i, -1, visited, disc, low, bridges, graph, time)
#
#     # Output
#     print("Important streets:")
#     for bridge in sorted(bridges):
#         print(f"{bridge[0]} {bridge[1]}")
#
# # Example execution
# # Uncomment the next line to test the program interactively
# find_important_streets()


from collections import defaultdict


def find_bridges(buildings, streets, connections):
    def dfs(at, parent, time):
        visited[at] = True
        ids[at] = low[at] = time
        time += 1

        for to in graph[at]:
            if to == parent:
                continue
            if not visited[to]:
                dfs(to, at, time)
                low[at] = min(low[at], low[to])
                if ids[at] < low[to]:
                    bridges.append(tuple(sorted((at, to))))
            else:
                low[at] = min(low[at], ids[to])

    # Build graph
    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * buildings
    ids = [-1] * buildings
    low = [-1] * buildings
    bridges = []

    # Run DFS to find bridges
    for i in range(buildings):
        if not visited[i]:
            dfs(i, -1, 0)

    return bridges

# Input
buildings = int(input())
streets = int(input())
connections = [tuple(map(int, input().split(" - "))) for _ in range(streets)]

# Find and print important streets
bridges = find_bridges(buildings, streets, connections)

print("Important streets:")
for bridge in sorted(bridges):
    print(f"{bridge[0]} {bridge[1]}")
