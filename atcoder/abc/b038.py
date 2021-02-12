(h1, w1), (h2, w2) = [map(int, input().split()) for _ in range(2)]
print("YES" if (h1 - h2) * (h1 - w2) * (w1 - h2) * (w1 - w2) == 0 else "NO")
