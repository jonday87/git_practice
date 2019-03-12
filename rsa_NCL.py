primes = [89, 181]
rsaNec = [
    [16109,47,3954],[16109,47,3634],[16109,47,10591],
    [16109,47,13428],[16109,47,10591],[16109,47,3911],
    [16109,47,10534],[16109,47,1873],[16109,47,13428],
    [16109,47,15075],[16109,47,2540],[16109,47,5050],[16109,47,2540],
]

# Find prime factorization for N
def findPrimeFactors(N):
    return [(p, q) for p in primes for q in primes if p * q == N][0]

# Extended Euclidian Algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Compute the inverse modulo
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def decrypt(c,d,N):
    return pow(c,d,N)

# Decrypt and print RSA data
for Nec in rsaNec:
    N,e,c = Nec
    p, q = findPrimeFactors(N)
    n=(p-1)*(q-1)
    d=modinv(e, n)
    try:
        print(chr(decrypt(c,d,N)))
    except Exception:
        print('Error in decryption')