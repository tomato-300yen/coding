S, T = [input() for _ in range(2)]
s_map = sorted(map(S.count, set(S)))
t_map = sorted(map(T.count, set(T)))
print("Yes" if s_map == t_map else "No")
