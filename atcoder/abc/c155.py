N = int(input())
S = [input() for _ in range(N)]
dict_count = dict()
for s in S:
    if s in dict_count.keys():
        dict_count[s] += 1
    else:
        dict_count[s] = 1
list_count = [[key, value] for key, value in dict_count.items()]
list_count.sort(key=lambda ll: (-ll[1], ll[0]))
print(list_count)
max_num = list_count[0][1]
for key, value in list_count:
    if value != max_num:
        break
    print(key)
