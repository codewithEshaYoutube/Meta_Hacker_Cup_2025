def solve():
    with open('snake_input.txt', 'r') as f:
        data = f.read().split()

    idx = 0
    T = int(data[idx]);
    idx += 1
    results = []

    for case_num in range(1, T + 1):
        N = int(data[idx]);
        idx += 1
        A = []
        for _ in range(N):
            A.append(int(data[idx]));
            idx += 1

        max_diff = 0
        for i in range(N - 1):
            max_diff = max(max_diff, abs(A[i] - A[i + 1]))

        results.append(f"Case #{case_num}: {max_diff}")

    with open('snake_output.txt', 'w') as f:
        for res in results:
            f.write(res + '\n')


if __name__ == "__main__":
    solve()