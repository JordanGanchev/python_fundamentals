import heapq

def parse_input():
    r = int(input())
    graph = {}
    for _ in range(r):
        road = input()
        city1, city2, distance = road.split(" - ")
        distance = int(distance)

        if city1 not in graph:
            graph[city1] = []
        if city2 not in graph:
            graph[city2] = []

        graph[city1].append((city2, distance))
        graph[city2].append((city1, distance))
    closed_roads_input = input()
    closed_roads = set()
    if closed_roads_input:
        for closed_road in closed_roads_input.split(","):
            city1, city2 = closed_road.split("-")
            closed_roads.add((city1, city2))
            closed_roads.add((city2, city1))
    start_city = input()
    end_city = input()

    return graph, closed_roads, start_city, end_city

def find_shortest_path(graph, closed_roads, start_city, end_city):
    pq = []
    heapq.heappush(pq, (0, start_city, []))  # (distance, current_city, path)
    visited = set()

    while pq:
        current_distance, current_city, path = heapq.heappop(pq)
        if current_city in visited:
            continue
        visited.add(current_city)
        path = path + [current_city]
        if current_city == end_city:
            return path, current_distance

        for neighbor, distance in graph.get(current_city, []):
            if neighbor not in visited and (current_city, neighbor) not in closed_roads:
                heapq.heappush(pq, (current_distance + distance, neighbor, path))

    return None, float('inf')  # No path found (should not happen due to problem constraints)


graph, closed_roads, start_city, end_city = parse_input()
path, total_distance = find_shortest_path(graph, closed_roads, start_city, end_city)

print(" - ".join(path))
print(total_distance)
