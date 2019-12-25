import math
import numpy as np


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def sgn(a):
    if a < 0:
        return -1
    else:
        return 1


def sgn2(a):
    if a < 0:
        return "-"
    else:
        return "+"


def tnf(a, b, c):
    x = "x"
    k = sgn(a) * gcd(gcd(a, b), c)
    aq = a / k
    bq = b / k
    cq = c / k

    if k == 1:
        k = ''
    if aq == 1:
        aq = ''
    if a == 1:
        a = ''
    return a, 'x\u00b2', sgn2(b), b, 'x', sgn2(c), c, '=', k, '(', aq, 'x\u00b2', sgn2(bq), bq, 'x', sgn2(cq), cq


def tf(a, b, c):
    x = 'x'
    d = (b * b) - (4 * a * c)
    if d < 0:
        return tnf(a, b, c)
    else:
        z = math.sqrt(d)
        t1 = sgn(a) * gcd(abs(-b - z), 2 * a)
        t2 = sgn(a) * gcd(abs(-b + z), 2 * a)
        r1 = (-b - z) / t1
        s1 = (2 * a) / t1
        r2 = (-b + z) / t2
        s2 = (2 * a) / t2
        h = a / (s1 * s2)
        if h == 1:
            if a == 1:
                a = ''
            if b == 1:
                b = ''
            if s1 == 1:
                s1 = ''
            if s2 == 1:
                s2 = ''
            return a, 'x\u00b2', sgn2(b), b, "x", sgn2(c), c, ' = ', '(', s1, 'x', sgn2(r1), -r1, ')(', s2, 'x', sgn2(
                r2), -r2
        else:
            return a, 'x\u00b2', sgn2(b), b, "x", sgn2(c), c, ' = ', h, '(', s1, 'x', sgn2(
                r1), -r1, ')(', s2, 'x', sgn2(
                r2), -r2


a = int(input("a: "))
b = int(input("b: "))
c = int(input('c: '))

t = tf(a, b, a)
y = str(t).replace(',', '')
z = str(y).replace("'", '')
o = str(z).replace('.0', '')
k = str(o).replace("1x", "x")
u = str(k).replace(' ', '')
print(u)
