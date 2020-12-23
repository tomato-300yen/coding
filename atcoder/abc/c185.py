import math


def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)


def combination(a, b):
    if a / 2 <= b:
        return combination(a, a - b)
    else:
        return permutations_count(a, b) // permutations_count(b, b)


def main():

    L = int(input())
    print(int(combination(L - 1, 11)))


if __name__ == "__main__":
    main()
