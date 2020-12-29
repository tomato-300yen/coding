def main():
    N = int(input())
    string = input()

    i = 0
    count = 0
    while True:
        if i >= N:
            break
        if string[i] != "A" and string[i] != "B" and string[i] != "C":
            i += 1
            continue
        if string[i:i + 3] == "ABC":
            count += 1
            i += 3
        else:
            i += 1
    print(count)


if __name__ == "__main__":
    main()
