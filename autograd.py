#kode for øving 2 vitber autograd.
# Fyll inn koden for b-spørsmålet her

#**(a)** Lag en funksjon *gNewton* som tar tre inputargumenter: funksjonen $f(x)$ som en skal finne nullpunkter til, startverdien $x^{(0)}$, og toleransen tol. Returner approksimert rot og antall iterasjoner.



import autograd.numpy as np
from autograd import value_and_grad



def f(x):
    # Fyll inn definisjon av den konkrete funksjonen f her

    return fval


def gNewton(f, x0, tol):
    

    assert tol>0
# Fyll in kode for gNewton her
    VG = value_and_grad(f) #returnerer en tuple med (Orginalfunksjon, derivertfunksjon)
    Values = VG(x0) #setter inn verdier i VG og returnerer funksjonsverdiene satt inn for x0.
    
    NMAX = 100
    difference = 2*tol
    xn = x0
    iter = 0

    print("iter     x")
    while difference>tol:
        iter = iter+1
        x = xn - Values[0]/Values[1]
        difference = abs(x - xn)
        xn = x
        if iter>NMAX:
            break
        print(repr(iter).rjust(0), repr(x).rjust(25))

# Utfør påkrevde tester under her

f = lambda x : x**2 #Some main function that is done nothing to yet.

answ = gNewton(f, x0, tol) #Answers the main goal

