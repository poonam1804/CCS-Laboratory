import math

# Step 1: Accept user input for prime numbers p and q
p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))

# Step 2: Compute n
n = p * q
print("n =", n)

# Step 3: Compute phi(n)
phi = (p - 1) * (q - 1)

# Step 4: Choose e such that 1 < e < phi and gcd(e, phi) = 1
e = 13
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    else:
        e += 1

print("e =", e)

# Step 5: Compute d (private key) using k such that d = (k*phi + 1)/e
if (math.gcd(phi,e)==1):
    for i in range (0,phi):
        if( ((phi*i)+1)%e==0):
            d= ((phi*i)+1)//e
            print(f"{d}  is a Private Key")
            break

print(f'Public key: ({e}, {n})')
print(f'Private key: ({d}, {n})')

# Accept user input for the message
msg = int(input("Enter the message (as an integer): "))
print(f'Original message: {msg}')

# Encryption
C=((msg^e)%n)
C = pow(msg,e,n)

print(f'Encrypted message: {C}')

# Decryption
M = ((C^d)%n)
M = pow(C,int(d),n)
print(f'Decrypted message: {M}')
