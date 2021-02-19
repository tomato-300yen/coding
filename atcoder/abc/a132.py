S = input()
for s in set(S):
    if S.count(s) != 2:
        print("No")
        break
else:
    print("Yes")
