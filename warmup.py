# Meta Hacker Cup 2025 - Problem A: Warm Up
# Author: Eesha Tariq

def solve():
    with open("input.txt", "r") as f:
        t = int(f.readline().strip())
        test_cases = []
        for _ in range(t):
            n = int(f.readline().strip())
            A = list(map(int, f.readline().strip().split()))
            B = list(map(int, f.readline().strip().split()))
            test_cases.append((n, A, B))
    
    results = []

    for case_num, (n, A, B) in enumerate(test_cases, 1):
        # If A and B are already same, no operation needed
        if A == B:
            results.append(f"Case #{case_num}: 0")
            continue
        
        # Sort both arrays with original indices to track operations
        indexed_A = sorted([(val, idx) for idx, val in enumerate(A)], key=lambda x: x[0])
        indexed_B = sorted([(val, idx) for idx, val in enumerate(B)], key=lambda x: x[0])

        possible = True
        for i in range(n):
            if indexed_A[i][0] > indexed_B[i][0]:
                possible = False
                break
        
        if not possible:
            results.append(f"Case #{case_num}: -1")
            continue

        ops = []
        A = indexed_A[:]
        B = indexed_B[:]

        # Try to match from highest to lowest
        for i in range(n - 1, -1, -1):
            if A[i][0] < B[i][0]:
                diff = B[i][0] - A[i][0]
                j = i - 1
                while j >= 0 and A[i][0] < B[i][0]:
                    if A[j][0] < B[i][0]:
                        A[j] = (B[i][0], A[j][1])
                        ops.append((A[i][1] + 1, A[j][1] + 1))
                    j -= 1

        if len(ops) > n:
            results.append(f"Case #{case_num}: -1")
        else:
            results.append(f"Case #{case_num}: {len(ops)}")
            for x, y in ops:
                results.append(f"{x} {y}")
    
    with open("output.txt", "w") as f:
        f.write("\n".join(results))

if __name__ == "__main__":
    solve()
