import random

# cek bilangan prima
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# cari FPB (Faktor Persekutuan Terbesar)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# cari nilai d
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception('Modular inverse tidak ditemukan')
    else:
        return x % phi
    
# generate public & private key
def generate_keypair(p = 61, q = 53):
    # p dan q adalah bilangan prima yang gede
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Kedua bilangan harus prima')
    elif p == q:
        raise ValueError('p dan q tidak boleh sama')
    
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537 # nilai standar
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2

    d = mod_inverse(e, phi)

    # (e, n) adalah Public Key, (d, n) adalah Private Key
    return ((e, n), (d, n))

# digita; signing
def sign(private_key, hashed_text):
    d, n = private_key

    hash_int = int(hashed_text, 16)

    # Rumus RSA Sign: S = M^d mod n
    signature = pow(hash_int, d, n)
    return signature

# verifikasi signature
def verify(public_key, signature, current_hash):
    e, n = public_key

    # Rumus RSA Verify: M' = S^e mod n
    decrypted_hash_int = pow(signature, e, n)
    decrypted_hash = hex(decrypted_hash_int)[2:].zfill(64)

    return decrypted_hash == current_hash