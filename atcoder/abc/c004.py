N = int(input())
cards = list(range(1, 7))
N = N % 30
for n in range(N // 5):
    cards = cards[1:] + cards[:1]
for n in range(N % 5):
    cards[n % 5], cards[n % 5 + 1] = cards[n % 5 + 1], cards[n % 5]
print("".join(map(str, cards)))
