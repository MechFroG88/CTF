from Crypto.Util.number import getPrime
import random

P = getPrime(1024)
Q = getPrime(1024)
N = P*Q
print('n = ' + str(N))
print('pp = ' + str(P+random.randint(-2**256,2**256)))