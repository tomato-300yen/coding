S = input()
last = ""
ans = False
for s in S:
    if s == last:
        ans = True
    last = s
print("Bad" if ans else "Good")
