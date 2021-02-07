N = input()
count = 1
last = ""
ans = False
for n in N:
    if n == last:
        count += 1
    else:
        count = 1
    if count == 3:
        ans = True
    last = n
print("Yes" if ans else "No")
