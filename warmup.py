# Warm Up — Meta Hacker Cup 2025 (Problem A)
# Read from stdin; print to stdout
# Usage: python solution.py < input.txt > output.txt

import sys
from collections import defaultdict, deque

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    T = int(next(it))

    out_lines = []

    for case in range(1, T + 1):
        n = int(next(it))
        A = [int(next(it)) for _ in range(n)]
        B = [int(next(it)) for _ in range(n)]

        # Quick impossible check: can't lower a temperature
        ok = True
        for i in range(n):
            if A[i] > B[i]:
                ok = False
                break
        if not ok:
            out_lines.append(f"Case #{case}: -1")
            continue

        # Group indices by their target temperature
        need_indices = defaultdict(list)
        for i, b in enumerate(B):
            need_indices[b].append(i)

        # Collect current heaters: values present in A and index list
        heaters = defaultdict(deque)
        for i, a in enumerate(A):
            # a is current temperature of dish i
            # if a already equals its target, it's definitely a heater for that temp
            # but we also want any position that currently has temp a to be a potential heater
            heaters[a].append(i)

        ops = []
        possible = True

        # Process each distinct target temperature.
        # Order doesn't strictly matter for correctness, but we iterate over
        # descending temperatures to match typical reasoning (not necessary).
        for temp in sorted(need_indices.keys(), reverse=True):
            indices = need_indices[temp]

            # If none of the dishes that should be temp currently are temp,
            # we still might have some other dish with that temp in A (heater).
            # We need at least one heater with value == temp if any dish needs temp.
            if not heaters.get(temp):
                # No current dish has exact temperature 'temp' to serve as heater.
                # If every dish already equals its target, that's fine (no need).
                # But if any dish needs to become 'temp', we cannot create 'temp'.
                # So impossible.
                # (We already checked A[i] <= B[i], but that doesn't help create new temps.)
                # However it's possible that some indices in `indices` already have A[i]==temp,
                # in which case heaters[temp] would have been filled above. So here heaters[temp] empty ⇒ impossible.
                # Therefore:
                # If all indices already A[i]==temp we would have had heaters, so simply impossible now.
                # So break.
                possible = False
                break

            # Use the first heater (any heater) as source to warm other non-matching dishes.
            # We'll reuse the same heater for all needed indices; every time we heat a dish to 'temp',
            # that dish becomes a heater too (so we append it).
            source = heaters[temp][0]

            for idx in indices:
                if A[idx] == temp:
                    # already correct, this index itself can be a heater (ensure it's in heaters[temp])
                    # make sure index is in heaters[temp]; duplicates are allowed but harmless
                    # avoid double-adding if it's already present by checking quickly:
                    # but it's ok to allow duplicates — they won't break correctness.
                    if idx not in heaters[temp]:
                        heaters[temp].append(idx)
                    continue

                # need to warm idx to 'temp' using some heater that already has 'temp'
                # pick source as heaters[temp][0]
                if not heaters[temp]:
                    possible = False
                    break

                h = heaters[temp][0]  # index of a dish currently at temp
                # operation warms dish idx (colder) to match h (hotter)
                ops.append((h + 1, idx + 1))  # 1-based indices for output
                A[idx] = temp
                # now idx becomes a heater as well
                heaters[temp].append(idx)

            if not possible:
                break

        if not possible or len(ops) > n:
            out_lines.append(f"Case #{case}: -1")
        else:
            out_lines.append(f"Case #{case}: {len(ops)}")
            for x, y in ops:
                out_lines.append(f"{x} {y}")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()
