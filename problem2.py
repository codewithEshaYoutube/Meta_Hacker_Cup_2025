from collections import deque


def solve_case(R, C, S, grid):
    # Multi-source BFS to find distance from each cell to nearest obstacle/wall
    dist = [[-1] * C for _ in range(R)]
    queue = deque()

    # Add all obstacles and walls to queue
    # Walls are implicit - cells on the boundary
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '#':
                dist[i][j] = 0
                queue.append((i, j))
            elif i == 0 or i == R - 1 or j == 0 or j == C - 1:
                # Boundary cells (walls)
                dist[i][j] = 0
                queue.append((i, j))

    # BFS to compute distances
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    # Find all safe cells (distance >= S)
    safe = [[False] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if dist[i][j] >= S:
                safe[i][j] = True

    # Find largest connected component of safe cells
    visited = [[False] * C for _ in range(R)]
    max_size = 0

    def bfs_component(start_r, start_c):
        queue = deque([(start_r, start_c)])
        visited[start_r][start_c] = True
        size = 1

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < R and 0 <= nc < C and
                        not visited[nr][nc] and safe[nr][nc]):
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    size += 1
        return size

    for i in range(R):
        for j in range(C):
            if safe[i][j] and not visited[i][j]:
                component_size = bfs_component(i, j)
                max_size = max(max_size, component_size)

    return max_size


def solve():
    T = int(input())
    for case_num in range(1, T + 1):
        R, C, S = map(int, input().split())
        grid = []
        for _ in range(R):
            grid.append(input().strip())

        result = solve_case(R, C, S, grid)
        print(f"Case #{case_num}: {result}")


if __name__ == "__main__":
    solve()