import sys

def solve():
    with open('snakes2_input.txt', 'r') as f:
        data = f.read().split()

    idx = 0
    T = int(data[idx]); idx += 1
    results = []

    for case_num in range(1, T + 1):
        N = int(data[idx]); idx += 1
        A = []
        for _ in range(N):
            A.append(int(data[idx])); idx += 1

        # Precompute max adjacent differences
        max_adj_diff = 0
        for i in range(N-1):
            max_adj_diff = max(max_adj_diff, abs(A[i] - A[i+1]))

        # The answer is min(max_adj_diff, max(A))
        # But we need to ensure connectivity from ground

        # More precise: answer is max(min(A[i]), max_adj_diff) ?
        # Actually, known formula for this problem:
        # We need to connect all platforms to ground via paths where max edge is minimized
        # The optimal h is max(min(A[i] for i in range(N)), max_adj_diff) ?
        # Let's think...

        # Actually, the correct observation:
        # We can always reach all platforms if h >= max(min_prefix, min_suffix)
        # where min_prefix[i] = min(A[0..i]) and we check connectivity

        # But the proven approach:
        # h must be at least the maximum of:
        # 1. The minimum height needed to connect all adjacent platforms (max adjacent diff)
        # 2. The minimum height needed to reach the highest platform from ground

        # Wait, let's implement the proven efficient solution:

        # We need to find minimal h such that:
        # - All platforms are connected in components where within each component,
        #   we can reach from ground if min height in component <= h
        # - And adjacent components are connected if their height difference <= h

        # The efficient O(N) solution:
        # Process from left to right, maintain current component's min height
        # When we can't connect to next platform, we need h >= current gap
        # Actually, known trick: answer = max( min(A), max_adj_diff )
        # Let's test with samples:

        # Sample 1: A=[2,4,5,1,4], min(A)=1, max_adj_diff=4, max(1,4)=4 but answer is 3
        # So that doesn't work.

        # Let's stick with binary search but optimize BFS to avoid deep recursion

        left = 0
        right = max(A)

        while left < right:
            mid = (left + right) // 2

            # Optimized BFS using iterative approach
            visited = [False] * N
            stack = []

            # Start from ground-connected platforms
            for i in range(N):
                if A[i] <= mid:
                    visited[i] = True
                    stack.append(i)

            # DFS using stack to avoid recursion depth issues
            while stack:
                i = stack.pop()

                # Left neighbor
                if i > 0 and not visited[i-1] and abs(A[i] - A[i-1]) <= mid:
                    visited[i-1] = True
                    stack.append(i-1)

                # Right neighbor
                if i < N-1 and not visited[i+1] and abs(A[i] - A[i+1]) <= mid:
                    visited[i+1] = True
                    stack.append(i+1)

            if all(visited):
                right = mid
            else:
                left = mid + 1

        results.append(f"Case #{case_num}: {left}")

    with open('snake2_output.txt', 'w') as f:
        for res in results:
            f.write(res + '\n')

if __name__ == "__main__":
    solve()