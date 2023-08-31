import numpy as np

q = 97

A = np.array([96, 50, 86, 69, 66, 46, 48, 30, 53, 17, 88, 59, 57, 84, 93, 24, 6, 74, 94, 61])

s = np.array(5)

e = np.array([3, 1, 2, 3, 3, 1, 1, 1, 2, 1, 1, 3, 4, 2, 4, 2, 4, 1, 2, 3])

partial_b = (A * s) % q

B = np.add(partial_b,e)%q

print("public key A\n", A)
print("public key B\n", B)

# Now encrypt the message m
# First need to perform sampling on A and B
# Choose 6 random indices from 0 to 19 and sample the corresponding elements of A and B

m=1

indices = np.random.choice(20,6,replace=False)
samples_a = np.take(A,indices)
samples_b = np.take(B,indices)

print("samples_a\n", samples_a)
print("samples_b\n", samples_b)

u = np.sum(samples_a)%q
v = (np.sum(samples_b)+ (q/2)*m) % q

print("u\n", u)
print("v\n", v)

# Now decrypt the ciphertext (u,v)
# result = v - s*u mod q
# If result < q/2 then dec=0 else dec=1

result = (v - s*u) % q

if result < q/2:
    dec=0
else:
    dec=1

print("result\n", result)
print("decrypted message\n", dec)