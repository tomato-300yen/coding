x, y = map(int, input().split())
set_list = []
set_list.append(set([1, 3, 5, 7, 8, 10, 12]))
set_list.append(set([4, 6, 9, 11]))
set_list.append(set([2]))
for st in set_list:
    if x in st and y in st:
        print("Yes")
        break
else:
    print("No")
