alphabet_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = int(input())
S = input()
ans = ""
for s in S:
    idx = alphabet_table.index(s)
    ans = ans + alphabet_table[(idx + N) % len(alphabet_table)]
print(ans)
