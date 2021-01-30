def main():
    A, B, C = list(map(int, input().split()))
    if C == 0:
        if A <= B:
            print("Aoki")
        else:
            print("Takahashi")
    else:
        if B <= A:
            print("Takahashi")
        else:
            print("Aoki")


if __name__ == "__main__":
    main()
