import numpy as np

import matplotlib
import matplotlib.pyplot as plt

def t_0(a_v, a_a, f_v, f_a):
    return 0.1 * (a_v * f_v) / (a_a * f_a)

def t_c(a_v, a_a, f_v, f_a):
    return 0.48 * (a_v * f_v) / (a_a * f_a)

def t_l(f_v):
    return 2.4 * f_v

def s_a(t, a_v, a_a, f_v, f_a, i):
    if t < t_c(a_v, a_a, f_v, f_a):
        return 2.5 * a_a * f_a * i
    elif t < t_l(f_v):
        return 1.2 * a_v * f_v * i / t
    else:
        return 1.2 * a_v * f_v * t_l(f_v) * i / t ** 2

def plot_espectro(a_v, a_a, f_v, f_a, i, step=0.01, end=10):
    x = np.arange(0, end, step)
    y = np.array([s_a(xi, a_v, a_a, f_v, f_a, i) for xi in x])

    fig, ax = plt.subplots()

    ax.plot(x, y)

    ax.set(xlabel='Período [s]', ylabel='aceleración de la gravedad', title='Espectro de aceleraciones')
    ax.grid()

    fig.savefig("espectro.png")


if __name__ == "__main__":
    a_v = a_a = 0.15
    f_v = f_a = 1
    i = 1.2

    plot_espectro(a_v, a_a, f_v, f_a, i)
