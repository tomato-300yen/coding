def main():
    a, b = tuple(map(int, input().split()))
    c, d = tuple(map(int, input().split()))
    print(a * d - b * c)


if __name__ == "__main__":
    main()
