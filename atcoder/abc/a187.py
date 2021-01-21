def count(num: int) -> int:
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum


def main():
    A, B = list(map(int, input().split()))
    sum_A = count(A)
    sum_B = count(B)
    if sum_A > sum_B:
        print(sum_A)
    else:
        print(sum_B)


if __name__ == "__main__":
    main()
