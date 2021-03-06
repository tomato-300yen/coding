import re
N, S = int(input()), input()
flag = re.match("^((cabcab)*cabca|(bcabca)*b|(abcabc)*abc)$", S)
print((N - 1) // 2 if flag else -1)
