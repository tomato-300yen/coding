def bs_decode(binary: str, key: str) -> int:
    sum = 0
    last_idx = 0
    for i, s in enumerate(binary):
        if s == '0':
            continue
        elif s == '1':
            sum += int(key[last_idx: i + 1])
            last_idx = i + 1
        else:
            assert False

    sum += int(key[last_idx:])
    return sum


def binary_search(binary: str, key: str) -> int:
    if len(binary) == len(key) - 1:
        return bs_decode(binary, key)
    else:
        return binary_search(binary + '0', key) + binary_search(binary + '1', key)


def main():
    S = input()
    print(binary_search('', S))


if __name__ == "__main__":
    main()
