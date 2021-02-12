A, B, C = map(int, input().split())
print("Yes" if (A <= C and C <= B) or (B <= C and C <= A) else "No")
