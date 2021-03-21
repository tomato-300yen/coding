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


def convolve_(f, g):
    """多項式 f, g の積を計算する。

    Parameters
    ----------
    f : np.ndarray (int64)
        f[i] に、x^i の係数が入っている

    g : np.ndarray (int64)
        g[i] に、x^i の係数が入っている


    Returns
    -------
    h : np.ndarray
        f,g の積
    """
    # h の長さ以上の n=2^k を計算
    fft_len = 1
    while 2 * fft_len < len(f) + len(g) - 1:
        fft_len *= 2
    fft_len *= 2

    # フーリエ変換
    Ff = np.fft.rfft(f, fft_len)
    Fg = np.fft.rfft(g, fft_len)

    # 各点積
    Fh = Ff * Fg

    # フーリエ逆変換
    h = np.fft.irfft(Fh, fft_len)

    # 小数になっているので、整数にまるめる
    h = np.rint(h).astype(np.int64)

    return h[: len(f) + len(g) - 1]


def convolve2(f, g, p):
    """
    多項式f, gの積をmod p で計算する。
    少数を経由するため計算誤差が生じるが、pが10^9程度、
    f, gの長さが250000以下程度であれば、正確に計算できる。
    """
    # f = 2^15 f_1 + f2 みたいに分解
    f1, f2 = np.divmod(f, 1 << 15)
    g1, g2 = np.divmod(g, 1 << 15)

    # h = 2^30 a + 2^15 b + c となるa, b, cを計算する
    # b については、b = f1g1 + f2g1 = (f1+f2)(g1+g2) - (f1g1 + f2g2)を利用
    a = convolve(f1, g1) % p
    c = convolve(f2, g2) % p
    b = (convolve(f1 + f2, g1 + g2) - (a + c)) % p

    h = (a << 30) + (b << 15) + c
    return h % p
