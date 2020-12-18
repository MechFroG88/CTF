from Crypto.Util.number import bytes_to_long, getPrime

e = 3
flag = b'flag{?????}'
m = bytes_to_long(flag)

P = getPrime(1024)
Q = getPrime(1024)
N = P*Q
m = m**2 + 3*m + 2**1000
print('e = ' + str(e))
print('n = ' + str(N))
print('c = ' + str(pow(m,e,N)))