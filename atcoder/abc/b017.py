X = input()
i = 0
while i < len(X):
    if X[i] == "c":
        if X[i + 1] != "h":
            print("NO")
            break
        i += 1
    elif X[i] == "o":
        pass
    elif X[i] == "k":
        pass
    elif X[i] == "u":
        pass
    else:
        print("NO")
        break
    i += 1
else:
    print("YES")
