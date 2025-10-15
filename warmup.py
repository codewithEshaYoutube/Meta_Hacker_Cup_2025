# Meta Hacker Cup 2025 - Problem A: Warm Up
# Usage:
#   python solution.py < input.txt > output.txt

import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    T = int(next(it))
    out = []

    for case in range(1, T + 1):
        n = int(next(it))
        A = [int(next(it)) for _ in range(n)]
        B = [int(next(it)) for _ in range(n)]

        if any(A[i] > B[i] for i in range(n)):
            out.append(f"Case #{case}: -1")
            continue

        available = set(A)
        if not set(B).issubset(available):
            out.append(f"Case #{case}: -1")
            continue

        target_indices = defaultdict(list)
        for i in range(n):
            target_indices[B[i]].append(i)

        heaters = defaultdict(list)
        for i in range(n):
            heaters[A[i]].append(i)

        unique_temps = sorted(set(B), reverse=True)
        ops = []

        for temp in unique_temps:
            if not heaters[temp]:
                out.append(f"Case #{case}: -1")
                break

            heater = heaters[temp][0]
            for idx in target_indices[temp]:
                if A[idx] == temp:
                    continue
                ops.append((heater + 1, idx + 1))
                A[idx] = temp
                heaters[temp].append(idx)
            else:
                continue
            break
        else:
            out.append(f"Case #{case}: {len(ops)}")
            for x, y in ops:
                out.append(f"{x} {y}")

    print("\n".join(out))

if __name__ == "__main__":
    solve()
