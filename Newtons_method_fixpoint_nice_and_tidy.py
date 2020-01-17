import numpy as np
x0 = 0
tol = 1E-10





def type_of_iteraton(fN,fF, x0,tol, method):
    NMAX = 100
    assert tol>0
    difference = 2*tol
    xn = x0
    iter = 0

    print("iter     x")
    while difference>tol:
        iter = iter+1
        if method == "Newtons":
            x = fN(xn)
        else:
            x = fF(xn)
        difference = abs(x - xn)
        xn = x
        if iter>NMAX:
            break
        #print(repr(iter).rjust(0), repr(x).rjust(25))


    return x,iter

f_Newton = lambda x: x - (x**5 - 3*x + 1)/(5*x**4 - 3)

f_fikspt = lambda x: 1 / 3 * (x ** 5 + 1)

method = ["Newtons", "Fikspunktiterasjons"]
method_iter = iter(method)



#Gjør kall til funksjoner som utfører eksperimenter her
N=0
for i in method:
    N +=1
    answer, it = type_of_iteraton(f_Newton, f_fikspt, x0, tol, next(method_iter))
    #print(answer)
    print('%s metode gir nullpunkt i x= %e etter %d iterasjoner med en toleranse på: %e' % (method[N-1], answer, it, tol))

