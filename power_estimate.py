"""
This module is used to determine the values that the dimmer
must be set to, in order to achieve various levels of power
dissipation (in this case, the levels 0,10...90,100%).

Because P(t)=V(t)*I(t), it is true that we can determine the
power dissipation in a specific amount of time by integrating
this equation. Here, we integrate for half a period of the
mains supply, because that is the period of the power (the
period of sin squared).

Then, for each value we want to determine, we brute-force the
solution by comparing the desired result to the result of each
iteration (the precision is user-determined). The mean value
is mapped through the MIN and MAX values of the dimmer, thus
providing us with a result - of course with an error.

"""

from numpy import sin, linspace, pi
from scipy.integrate import quad
from math import floor, ceil

f = 50          # mains frequency
V = 325         # Vrms*sqrt(2)
I = 0.3         # 100/V because we work with percentages
HALF_P = 0.5/f  # half period of the wave
DIM_MAX = 600   # max value dictated by the dimmer..
DIM_MIN = 50    # .. and min value
PREC = 2        # precision for calculations


def integrand(x):
    return V*I*sin(2*pi*f*x)**2

MAX, _ = quad(integrand, 0, HALF_P)
for i in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
    power = MAX*i
    estimate = [floor(power*(10**PREC)), ceil(power*(10**PREC))]
    results = []

    for start in linspace(0, HALF_P, 500):
        res, _ = quad(integrand, start, HALF_P)
        #print res
        if int(res*(10**PREC)) in estimate:
            results.append(start)

    mean = sum(results)/len(results)
    solution = int(DIM_MAX*mean/HALF_P + DIM_MIN)

    print solution, int(i*100), '%'
