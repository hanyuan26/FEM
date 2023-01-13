import sympy as sy
import numpy as np

r, s, t = sy.symbols('r, s, t')


class C():
    def __init__(self, E, *material):
        pass

class PlainStress(C):
    def __init__(self, E, miu):
        super().__init__(E)
        self.n = 3
        self.C = np.zeros((self.n, self.n))
        self.E = E
        self.miu = miu

    def cal_C(self):
        temp_c0 = [1, 1, 0.5 * (1 - self.miu)]
        temp_c1 = [self.miu, 0]
        c0 = [(i * (self.E / (1 - self.miu ** 2))) for i in temp_c0]
        c1 = [(i * (self.E / (1 - self.miu ** 2))) for i in temp_c1]
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    self.C[i][j] = c0[i]
                elif 0 < j - i < 2 and i < 2:
                    self.C[i][j] = c1[i]
                elif 0 < i - j < 2:
                    self.C[i][j] = self.C[j][i]
        return self.C


if __name__ == "__main__":
    c = PlainStress(1, 0.3)
    print(c.cal_C())

