
S = input()


def bs(idx, _sum, l_char):
    if idx == 4:
        if _sum == 7:
            print(''.join(l_char) + '=7')
            return True
    elif idx == 0:
        _sum = int(S[idx])
        bs(idx + 1, _sum, l_char + [S[idx]])
    else:
        diff = int(S[idx])
        if bs(idx + 1, _sum + diff, l_char + ['+', S[idx]]):
            return True
        else:
            if bs(idx + 1, _sum - diff, l_char + ['-', S[idx]]):
                return True
            else:
                False


bs(0, 0, [])
