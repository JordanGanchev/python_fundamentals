from collections import deque

def shortest_path_in_maze(n, maze):

    start, end = None, None
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([(start, 0)])

    visited = set()
    visited.add(start)

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy


            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and maze[nx][ny] != '#':
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
    return -1

n = int(input())
maze = [input().strip() for _ in range(n)]

print(shortest_path_in_maze(n, maze))