import numpy as np

import matplotlib
import matplotlib.pyplot as plt

def f_v(tipo_suelo, a_v):
    tipo_suelo.lower()

    if tipo_suelo == 'a':
        return 0.8
    elif tipo_suelo == 'b':
        return 1
    elif tipo_suelo == 'c':
        if a_v < 0.10:
            return 1.7
        else:
            return 0.1 - (a_v - 0.1)
    elif tipo_suelo == 'd':
        if a_v < 0.1:
            return 2.4
        elif a_v < 0.2:
            return 2.4 - 4*(a_v -0.1)
        elif a_v < 0.4:
            return 2 - 2*(a_v - 0.2)
        else:
            return 1.6 - (a_v - 0.4)
    elif tipo_suelo == 'e':
        if a_v < 0.1:
            return 3.5
        elif a_v < 0.2:
            return 3.5 - 3*(a_v - 0.1)
        elif a_v < 0.4:
            return 3.2 - 4*(a_v - 0.2)
        else:
            return 2.4

def f_a(tipo_suelo, a_a):
    tipo_suelo.lower()

    if tipo_suelo == 'a':
        return 0.8
    elif tipo_suelo == 'b':
        return 1
    elif tipo_suelo == 'c':
        if a_v < 0.2:
            return 1.2
        elif a_v < 0.4:
            return 1.2 - (a_v - 0.2)
        else:
            return 1
    elif tipo_suelo == 'd':
        if a_v < 0.1:
            return 1.6
        elif a_v < 0.3:
            return 1.6 - 2*(a_v - 0.1)
        else:
            return 1.2 - (a_v - 0.3)

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
