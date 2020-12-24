def dp(table, x, y, z):
    if x == 100 or y == 100 or z == 100:
        return 0
    if table[x][y][z] != -1:
        return table[x][y][z]
    else:
        sum = 0
        if x != 0:
            dp_x = dp(table, x + 1, y, z)
            table[x + 1][y][z] = dp_x
            increase_x = (dp_x + 1) * x / (x + y + z)
            sum += increase_x
        if y != 0:
            dp_y = dp(table, x, y + 1, z)
            table[x][y + 1][z] = dp_y
            increase_y = (dp_y + 1) * y / (x + y + z)
            sum += increase_y
        if z != 0:
            dp_z = dp(table, x, y, z + 1)
            table[x][y][z + 1] = dp_z
            increase_z = (dp_z + 1) * z / (x + y + z)
            sum += increase_z
        table[x][y][z] = sum
        return sum


def main():
    A, B, C = list(map(int, input().split()))
    table = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(101)]
    # print(len(table[0][0]))
    # print(table[0][0][0])

    ans = dp(table, A, B, C)
    print(ans)


if __name__ == "__main__":
    main()
