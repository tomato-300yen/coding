N = int(input())
bad_set = set(
    [
        "AGC",
        "ACG",
        "GAC",
        "AGAC",
        "AGGC",
        "AGCC",
        "AGTC",
        "AAGC",
        "AGGC",
        "ACGC",
        "ATGC",
    ]
)


def dfs(a, b, c, d, num, length):
    """
    a,b,c : 直前3つの文字
    d : 追加しようとしている文字
    num : 現時点での題意を満たす文字列の数
    """
    tmp1 = b + c + d
    tmp2 = a + b + c + d
    if tmp1 in bad_set or tmp2 in bad_set:
        return 0
    else:
        if length == N:
            return num
        else:
            return (
                dfs(b, c, d, "A", num, length + 1)
                + dfs(b, c, d, "G", num, length + 1)
                + dfs(b, c, d, "T", num, length + 1)
                + dfs(b, c, d, "C", num, length + 1)
            ) % (10 ** 9 + 7)


print(
    (
        dfs("x", "x", "x", "A", 1, 1)
        + dfs("x", "x", "x", "T", 1, 1)
        + dfs("x", "x", "x", "G", 1, 1)
        + dfs("x", "x", "x", "C", 1, 1)
    )
    % (10 ** 9 + 7)
)
