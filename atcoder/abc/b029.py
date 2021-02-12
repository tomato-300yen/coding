S = [input() for _ in range(12)]
print(sum(map(lambda s: int("r" in s), S)))
