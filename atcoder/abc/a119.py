S = input()
year = int(S[:4])
month = int(S[5:7])
day = int(S[-2:])
if year < 2019:
    print("Heisei")
elif year > 2019:
    print("TBD")
elif month <= 4:
    print("Heisei")
elif month > 4:
    print("TBD")
