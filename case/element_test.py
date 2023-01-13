import sympy as sy
import numpy as np


from material_test import PlainStress


r, s, t = sy.symbols('r, s, t')

"""
P329
第一步实现J的计算
"""
class C2N4():
    def __init__(self):
        self.h = [0.25*(1+r)*(1+s), 0.25*(1-r)*(1+s), 0.25*(1-r)*(1-s), 0.25*(1+r)*(1-s)]
        self.integral_point = []
        self.local_point = [[3, 2], [-3, 2], [-3, -2], [3, -2]]
        self.J = [[0, 0], [0, 0]]
        self.B = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

    def cal_diff_h(self):
        self.diff_h = []
        diff_hr = [sy.diff(hi, r) for hi in self.h]
        diff_hs = [sy.diff(hi, s) for hi in self.h]
        self.diff_h.extend(diff_hr)
        self.diff_h.extend(diff_hs)
        return self.diff_h



    def cal_J(self):
        for i in range(2):
            for j in range(2):
                for k in range(4):
                    self.J[i][j] += self.local_point[k][j] * self.diff_h[k+4*i]
        return self.J
    """暂时还没有办法求J的行列式。"""

    def cal_B(self):
        for i in range(3):
            for j in range(8):
                if i == 0 and j % 2 == 0:
                    self.B[i][j] = self.diff_h[int((j+1)/2)]
                elif i == 1 and j % 2 != 0:
                    self.B[i][j] = self.diff_h[int(j/2)+4]
                elif i == 2:
                    temp_k = [4, -1, 3, -2, 2, -3, 1, -4]
                    self.B[i][j] = self.diff_h[(j+temp_k[j])]
        return self.B

    def cal_stiffness_matrix(self, C):
        temp_BC = [[0 for _ in range(8)] for _ in range(3)]
        self.BCB = [[0 for _ in range(8)] for _ in range(8)]
        for i in range(3):
            for j in range(8):
                for k in range(3):
                    temp_BC[i][j] += C[i][k] * self.B[k][j]
        for i in range(8):
            for j in range(8):
                for k in range(3):
                    self.BCB[i][j] += self.B[k][i] * temp_BC[k][j]
        return self.BCB



if __name__ == '__main__':
    element_c2n4 = C2N4()
    print(element_c2n4.cal_diff_h())
    print(type(element_c2n4.cal_J()[0][0]))
    print(element_c2n4.cal_B())
    plainstress_c = PlainStress(1, 0)
    c = plainstress_c.cal_C()
    print(element_c2n4.cal_stiffness_matrix(c))