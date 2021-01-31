def main() -> None:
    slot = input()
    if slot[0] == slot[1] and slot[1] == slot[2]:
        print("Won")
    else:
        print("Lost")


if __name__ == "__main__":
    main()
