def bin_search(bit_str, N, s_list, p_list):
    if len(bit_str) == N:
        num_on = 0
        # それぞれの電球の条件に関してfor
        for i, each_s in enumerate(s_list):
            count = 0
            for s in each_s:
                # print(bit_str, s)
                if bit_str[s - 1] == "1":
                    count += 1
            if count % 2 == p_list[i]:
                num_on += 1
        if num_on == len(p_list):
            return 1
        else:
            return 0
    else:
        return bin_search(bit_str + '0', N, s_list, p_list) + bin_search(bit_str + '1', N, s_list, p_list)


def main():
    N, M = tuple(map(int, input().split()))

    s_list = []
    for i in range(M):
        s_l = list(map(int, input().split()))[1:]
        s_list.append(s_l)
    p_list = list(map(int, input().split()))
    ans = bin_search('', N, s_list, p_list)
    print(ans)


if __name__ == "__main__":
    main()
