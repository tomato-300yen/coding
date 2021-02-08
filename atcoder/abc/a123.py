X = [int(input()) for _ in range(5)]
k = int(input())
max_ = 0
for i in range(len(X)):
    for j in range(i, len(X)):
        max_ = max(max_, abs(X[i] - X[j]))
print(":(" if max_ > k else "Yay!")
