from collections import Counter
N = int(input())
A = list(map(int, input().split()))
A_k = sorted(set(A))
A_c = Counter(A)
e_list = []
for a in A_k[::-1]:
    if A_c[a] >= 4:
        if len(e_list) == 0:
            print(a ** 2)
            break
        else:
            A_c[a] = A_c[a] - 2
            e_list.append(a)
    elif A_c[a] >= 2:
        A_c[a] = A_c[a] - 2
        e_list.append(a)

    if len(e_list) == 2:
        print(e_list[0] * e_list[1])
        break
else:
    print(0)
