import numpy as np

q=13

A=np.array([[4 ,1, 11, 10],[5, 5 ,9 ,5],[3, 9 ,0 ,10],[1, 3 ,3 ,2],[12, 7 ,3 ,4],[6, 5 ,11 ,4],[3, 3, 5, 0]])

s = np.array([[6],[9],[11],[11]])

e = np.array([[0],[-1],[1],[1],[1],[0],[-1]])

partial_b = np.matmul(A,s)%q
B = np.add(partial_b,e)%q

print(A)
print()
print(B)

