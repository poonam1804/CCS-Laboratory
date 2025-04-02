from Crypto.Cipher import DES
from secrets import token_bytes

key = token_bytes(8)

def encrypt(msg):
    cipher = DES.new(key, DES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return cipher.nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    try:
        plaintext = cipher.decrypt(ciphertext)
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

# Main logic
nonce, ciphertext, tag = encrypt(input('Enter a message: '))
plaintext = decrypt(nonce, ciphertext, tag)

print(f'Cipher text: {ciphertext}')
print(f'Plain text: {plaintext if plaintext else "Message is corrupted!"}')