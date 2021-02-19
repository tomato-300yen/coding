W = input()
for w in set(W):
    if W.count(w) % 2 != 0:
        print("No")
        break
else:
    print("Yes")
