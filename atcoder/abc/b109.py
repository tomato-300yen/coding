N = int(input())
first_word = input()
W = [input() for _ in range(N - 1)]
last = first_word[-1]
word_set = set([first_word])
for w in W:
    if w[0] != last or w in word_set:
        print("No")
        break
    word_set.add(w)
    last = w[-1]
else:
    print("Yes")
