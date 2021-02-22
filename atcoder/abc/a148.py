A, B = [int(input()) for _ in range(2)]
print(*(set([1, 2, 3]) - set([A, B])))
