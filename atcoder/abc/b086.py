a, b = input().split()
print("Yes" if (int(a + b) ** (1 / 2)).is_integer() else "No")
