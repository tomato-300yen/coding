weekday_list = [
    "MON",
    "TUE",
    "WED",
    "THU",
    "FRI",
    "SAT",
    "SUN",
]
idx = len(weekday_list) - weekday_list.index(input()) - 1
print(7 if idx == 0 else idx)
