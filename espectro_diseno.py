import numpy as np

import matplotlib
import matplotlib.pyplot as plt

class AnalisisDinamico:
    def __init__(self, a_v, a_a, tipo_suelo, grupo_uso):
        self.a_v = a_v
        self.a_a = a_a
        self.tipo_suelo = tipo_suelo
        self.grupo_uso = grupo_uso

    def f_v(self):
        tipo_suelo = self.tipo_suelo.lower()

        if tipo_suelo == 'a':
            return 0.8
        elif tipo_suelo == 'b':
            return 1
        elif tipo_suelo == 'c':
            if self.a_v < 0.10:
                return 1.7
            else:
                return 0.1 - (self.a_v - 0.1)
        elif tipo_suelo == 'd':
            if self.a_v < 0.1:
                return 2.4
            elif self.a_v < 0.2:
                return 2.4 - 4*(self.a_v -0.1)
            elif self.a_v < 0.4:
                return 2 - 2*(self.a_v - 0.2)
            else:
                return 1.6 - (self.a_v - 0.4)
        elif tipo_suelo == 'e':
            if self.a_v < 0.1:
                return 3.5
            elif self.a_v < 0.2:
                return 3.5 - 3*(self.a_v - 0.1)
            elif self.a_v < 0.4:
                return 3.2 - 4*(self.a_v - 0.2)
            else:
                return 2.4

    def f_a(self):
        tipo_suelo = self.tipo_suelo.lower()
        
        if tipo_suelo == 'a':
            return 0.8
        elif tipo_suelo == 'b':
            return 1
        elif tipo_suelo == 'c':
            if self.a_a < 0.2:
                return 1.2
            elif self.a_a < 0.4:
                return 1.2 - (self.a_a - 0.2)
            else:
                return 1
        elif tipo_suelo == 'd':
            if self.a_a < 0.1:
                return 1.6
            elif self.a_a < 0.3:
                return 1.6 - 2*(self.a_a - 0.1)
        else:
            return 1.2 - (self.a_a - 0.3)

    def i(self):
        if self.grupo_uso == 1:
            return 1
        elif self.grupo_uso == 2:
            return 1.1
        elif self.grupo_uso == 3:
            return 1.25
        else:
            return 1.5

    def t_0(self):
        return 0.1 * (self.a_v * self.f_v()) / (self.a_a * self.f_a())

    def t_c(self):
        return 0.48 * (self.a_v * self.f_v()) / (self.a_a * self.f_a())

    def t_l(self):
        return 2.4 * self.f_v()
    
    def s_a(self, t):
        if t < self.t_c():
            return 2.5 * self.a_a * self.f_a() * self.i()
        elif t < self.t_l():
            return 1.2 * self.a_v * self.f_v() * self.i() / t
        else:
            return 1.2 * self.a_v * self.f_v() * self.t_l() * self.i() / t ** 2

    def plot_espectro(self, step=0.01, end=10, save_as='espectro_diseno.png'):
        f_v = self.f_v()
        f_a = self.f_a()
        i = self.i()

        x = np.arange(0, end, step)
        y = np.array([self.s_a(xi) for xi in x])

        fig, ax = plt.subplots()

        ax.plot(x, y)

        ax.set(xlabel='Período [s]', ylabel='aceleración de la gravedad', title='Espectro de aceleraciones')
        ax.grid()

        fig.savefig(save_as)

        
if __name__ == "__main__":
    a_v = a_a = 0.15
    f_v = f_a = 1
    i = 1.2

    plot_espectro(a_v, a_a, f_v, f_a, i)
