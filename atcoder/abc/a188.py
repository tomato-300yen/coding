import math


def main():

    X, Y = list(map(int, input().split()))
    if math.fabs(X - Y) <= 2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
