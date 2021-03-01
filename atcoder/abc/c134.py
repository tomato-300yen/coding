N = int(input())
A = [int(input()) for _ in range(N)]
sorted_A = sorted(A)[::-1]
for a in A:
    is_skipped = False
    for a_ in sorted_A:
        if a == a_ and not is_skipped:
            is_skipped = True
            continue
        print(a_)
        break
