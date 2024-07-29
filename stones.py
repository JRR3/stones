import matplotlib as mpl
import numpy as np

class Stones:
    def __init__(self):
        pass

    def w_fun(self,x,y):
        val = 0
        for s in range(1,101):
            cos_sq = np.cos(s * s)
            sin_sq = np.sin(s * s)
            a1  = 5+s
            a1 *= cos_sq * x + sin_sq * y
            a1 += 10 * np.sin(10 * s)

            a = np.cos(a1)
            a = a**10

            a1  = 5+s
            a1 *= sin_sq * x - cos_sq * y
            a1 += 10 * np.sin(9 * s)

            b = np.cos(a1)
            b = b**10

            c = a * b - 0.5
            c *= 1000
            c = np.exp(-c)
            c = np.exp(-c)

            val += c
        
        return val / 100

    def c_fun(self,x,y):
        atan_arg = x + y/4 + 7/50
        atan_arg = -200 * np.abs(atan_arg) + 14
        a  = 1/2 + 1/np.pi * np.arctan(atan_arg)
        a *= 170 * (x + y/4 + 7/100)
        a += 35
        a *= 70
        b = y - x/4 - 1/2 - 2/5 * (x + y/4 - 1/20)**2
        b = np.abs(b)
        b = np.pow(b, 2 + 3/2 * (x + y/4 + 1/5))
        a *= b
        b = np.abs(x + y/4 + 1/5)
        b = np.pow(b, 5/2)
        b = 70 * b - 49/10
        a += b
        a = np.exp(a)
        a = np.exp(-a)

        return a

    def q_fun(self,s,x,y):
        a = 4 + np.cos(29 * s)
        a *= y
        b = 3 + np.cos(31 * s)
        b *= x
        b = np.cos(b)
        c = 5 * np.cos(6 * s)
        a = np.cos(a + b + c)
        a = x + 3/25 * a
        b = 4 + 3/5 * np.cos(8 * s)
        a = b * a + 3 * np.cos(9 * s)

        return a

    def p_fun(self,s,x,y):
        a = 4 + np.cos(19 * s)
        a *= x
        b = 3 + np.cos(34 * s)
        b *= y
        b = np.cos(b)
        c = 5 * np.cos(9 * s)
        a = np.cos(a + b + c)
        a = y + 3/25 * a
        b = 4 + 3/5 * np.cos(4 * s)
        a = b * a + 3 * np.cos(7 * s)

        return a

    def k_fun(self,s,x,y):
        a = self.q_fun(s,x,y)
        a = np.sin(a)
        b = self.p_fun(s,x,y)
        b = np.sin(b)
        a = np.pow(a * b, 6)
        a += -19/1000
        a = np.exp(-60 * a)
        a = np.exp(-a)

        return a

    def j_fun(self,v,s,x,y):
        a = self.q_fun(s,x,y)
        a = np.sin(a)
        b = self.p_fun(s,x,y)
        b = np.sin(b)
        a = np.pow(a * b, 6)
        a += -3/100
        a = np.exp(v * a)
        b = s - 0.5
        b = np.exp(-1000 * b)
        a = np.exp(-b - a)

        return a

    def e_fun(self,v,s,x,y):
        a = 7/10
        b = np.cos(14 * s)
        b *= (v - v*v + 2) / 40
        a += b

        b = np.cos(16 * s)
        b *= (3 * v - v*v) / 20
        a += b

        b = self.p_fun(s,x,y)
        b = np.sin(b)
        b = np.exp(-1000 * b)
        b = np.exp(-b)
        b *= (v*v - v) / 20
        a -= b

        b = self.p_fun(s,x,y)
        b = np.sin(b / 2)
        b = np.exp(-1000 * b)
        b = np.exp(-b)
        b *= (2 - 3 * v + v*v) / 20
        a += b

        b = self.q_fun(s,x,y)
        b = np.sin(b)
        b = np.exp(-1000 * b)
        b = np.exp(-b)
        b *= (v*v - v) / 20
        a += b

        b = self.q_fun(s,x,y)
        b = np.sin(b / 2)
        b = np.exp(-1000 * b)
        b = np.exp(-b)
        b *= (- 3 * v*v + 7 * v) / 40
        a += b

        return a

    def a_fun(self,v,x,y):
        val = 0
        for s in range(1,51):
            p = 1
            for u in range(s):
                p *= 1 - self.j_fun(-400,u,x,y)
            a = 1/2
            a += 1 / 2 * self.j_fun(-3,s,x,y)
            a -= 4 / 5 * self.j_fun(20,s,x,y)
            a *= self.j_fun(-400,s,x,y)

            b = self.k_fun(s,x,y)
            b -= self.j_fun(-400,s,x,y)
            b *= 1/2

            a -= b
            a *= p

            b = (11 + np.cos(12 * s)) / 10
            a *= b

            b = self.w_fun(x,y)
            b *= 4 + 2 * np.cos(3 * s)
            b = self.e_fun(v,s,x,y) - b
            a *= b

            val += a

        return val

    def h_fun(self,v,x,y):
        a = self.a_fun(v,x,y)


