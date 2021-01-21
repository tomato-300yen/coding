def main():
    _ = input()
    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split()))
    sum = 0
    for a, b in zip(list_A, list_B):
        sum += a * b
    if sum == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
