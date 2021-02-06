def main():
    N = int(input())
    S = [input() for _ in range(N)]
    dict_counter = dict()
    for each_s in S:
        if each_s[0] == "!":
            querry = each_s[1:]
            if querry in dict_counter.keys():
                dict_counter[querry][1] = 1
            else:
                dict_counter[querry] = [0, 1]
        else:
            querry = each_s
            if querry in dict_counter.keys():
                dict_counter[querry][0] = 1
            else:
                dict_counter[querry] = [1, 0]

    for key, value in dict_counter.items():
        if value[0] == 1 and value[1] == 1:
            print(key)
            return
    print("satisfiable")


if __name__ == "__main__":
    main()
