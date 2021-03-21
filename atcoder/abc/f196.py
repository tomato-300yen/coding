import numpy as np


def convolve(f, g):
    fft_len = 1
    while fft_len < len(f) + len(g) - 1:
        fft_len *= 2
    Ff = np.fft.rfft(f, fft_len)
    Fg = np.fft.rfft(g, fft_len)
    Ffg = Ff * Fg
    fg = np.fft.irfft(Ffg, fft_len)
    fg = np.rint(fg).astype(np.int64)
    return fg[: len(f) + len(g) - 1]


S = input()
T = input()
N = len(S)
M = len(T)
S1 = np.array(list(map(int, S)))
S2 = 1 - S1
T1 = np.array(list(map(int, reversed(T))))
T2 = 1 - T1
ans = convolve(S1, T2) + convolve(S2, T1)
print(np.min(ans[M - 1 : N]))
