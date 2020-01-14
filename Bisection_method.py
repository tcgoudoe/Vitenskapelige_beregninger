import numpy as np

# INPUT: Function f,
#       endpoint values a, b, 
#       tolerance TOL, 
#       maximum iterations NMAX
# CONDITIONS: a < b,
#            either f(a) < 0 and f(b) > 0 or f(a) > 0 and f(b) < 0
# OUTPUT: value which differs from a root of f(x) = 0 by less than TOL
# 
# N ← 1
# while N ≤ NMAX do // limit iterations to prevent infinite loop
#    c ← (a + b)/2 // new midpoint
#    if f(c) = 0 or (b – a)/2 < TOL then // solution found
#        Output(c)
#        Stop
#    end if
#  N ← N + 1 // increment step counter
#  if sign(f(c)) = sign(f(a)) then a ← c else b ← c // new interval
# end while
# Output("Method failed.") // max number of steps exceeded

# def inthalv(f,a,b,tol): osv

a = -1.5
b = 1.5
tol = 1E-7
NMAX = 100


def f(x):
    return 1 / 2 + 2 / 5 * x - np.exp(-16 * x ** 2)


def inthalv(a, b, tol):
    if f(a) * f(b) > 0:
        print("Ingen røtter")
    else:
        N = 1
        while N <= NMAX and (b - a) / 2 > tol:
            m = (a + b) / 2  # New point.
            if f(m) == 0:
                return m
            elif f(a) * f(m) < 0:
                b = m
            else:
                a = m
            N += 1

        return m



ans = inthalv(a, b, tol)
print(ans)