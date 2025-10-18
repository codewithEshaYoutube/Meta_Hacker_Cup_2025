from collections import deque

def solve_case(R, C, S, grid):
    dist = [[-1] * C for _ in range(R)]
    q = deque()
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    # Multi-source BFS from all walls (#) and implicit grid boundaries
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '#':
                dist[i][j] = 0
                q.append((i, j))
            elif i == 0 or i == R-1 or j == 0 or j == C-1:
                # boundary cells = adjacent to outer wall
                dist[i][j] = 0
                q.append((i, j))

    # BFS to compute distance from each cell to nearest wall/obstacle
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    # Mark safe cells (distance >= S)
    safe = [[dist[i][j] >= S for j in range(C)] for i in range(R)]

    # Find largest connected region of safe cells
    visited = [[False]*C for _ in range(R)]
    max_size = 0

    def bfs_component(sr, sc):
        q = deque([(sr, sc)])
        visited[sr][sc] = True
        size = 1
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and safe[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    size += 1
        return size

    for i in range(R):
        for j in range(C):
            if safe[i][j] and not visited[i][j]:
                max_size = max(max_size, bfs_component(i, j))

    return max_size


def solve_from_file(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read().strip().split('\n')

    T = int(data[0])
    idx = 1
    results = []

    for case_num in range(1, T+1):
        R, C, S = map(int, data[idx].split())
        idx += 1
        grid = [data[idx + i].strip() for i in range(R)]
        idx += R

        res = solve_case(R, C, S, grid)
        results.append(f"Case #{case_num}: {res}")

    with open(output_file, 'w') as f:
        f.write("\n".join(results))

    print(f"✅ Output written to {output_file}")


if __name__ == "__main__":
    solve_from_file("zone_in_input.txt", "zone_in_output.txt")
