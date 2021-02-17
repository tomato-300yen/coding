S = input()
scale_list = ["Do", "", "Re", "", "Mi", "Fa", "", "So", "", "La", "", "Si"]
order = "WBWBWWBWBWBW" * 3
print(scale_list[order.find(S)])
