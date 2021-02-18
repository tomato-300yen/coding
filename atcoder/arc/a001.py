N = int(input())
C = input()
S = ["1", "2", "3", "4"]
max_ = -1
min_ = 101
ans_list = []
for num in S:
    hit = list(C).count(num)
    ans_list.append(hit)
print(max(ans_list), min(ans_list))
