# Meta Hacker Cup 2025 - Problem A: Warm Up
# Run as: python solution.py < input.txt > output.txt

import sys

def solve():
    t = int(sys.stdin.readline())
    for case_num in range(1, t + 1):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))

        # Check impossible cases
        if any(a[i] > b[i] for i in range(n)):
            print(f"Case #{case_num}: -1")
            continue

        # If already equal
        if a == b:
            print(f"Case #{case_num}: 0")
            continue

        # If target has a new temperature that doesn't exist in a
        if not set(b).issubset(set(a)):
            print(f"Case #{case_num}: -1")
            continue

        # Simplified valid case handling (greedy simulation)
        ops = []
        possible = True

        while a != b:
            changed = False
            for i in range(n):
                if a[i] < b[i]:
                    heater_temp = b[i]
                    if heater_temp not in a:
                        possible = False
                        break
                    for j in range(n):
                        if b[j] == heater_temp and a[j] < b[j]:
                            a[j] = heater_temp
                            ops.append((a.index(heater_temp) + 1, j + 1))
                    changed = True
                    break
            if not changed or not possible:
                possible = False
                break

        if not possible:
            print(f"Case #{case_num}: -1")
        else:
            print(f"Case #{case_num}: {len(ops)}")
            for op in ops:
                print(*op)

if __name__ == "__main__":
    solve()
