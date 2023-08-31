import numpy as np
import numpy.polynomial.polynomial as p

# A polynomial is represented by their coefficients, starting from the constant term (degree 0)
A = [4,1,11,10] 
s = [6,9,11,11]
e =[0,-1,1,1]
n=4

q=13

xN_1 = [1] + [0] * (n-1) + [1] # This is the ring

A = np.floor(p.polydiv(A,xN_1)[1])
b_partial = p.polymul(A,s)%q
b_partial = np.floor(p.polydiv(b_partial,xN_1)[1])
b_partial = p.polyadd(b_partial,e)%q
B = np.floor(p.polydiv(b_partial,xN_1)[1])

print(B)
