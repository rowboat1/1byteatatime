import aes
import os
import time
import base64

# You might already know how to decode base64, but don't do it directly!
# This is about decrypting AES (what if you didn't have access to this secret?)
secret = base64.b64decode("cmljZXBhcGVycm9sbA==")
key = os.urandom(16)

def pad(text):
    if type(text) == bytes:
        return text + b"_" * (16 - len(text)%16)
    else:
        return text + "_" * (16 - len(text)%16)

def show_plaintext_blocks(plaintext):
    output = plaintext.replace(secret, b"*" * len(secret))
    # print(plaintext)
    print("YOUR INPUT:")
    for x in range(0, len(output), 16):
        print(output[x:x+16])

def encrypt(plaintext):
    plaintext = pad(plaintext)
    show_plaintext_blocks(plaintext)
    encrypted_new = aes.AES(key).encrypt_ecb(plaintext)
    return encrypted_new.hex()

def register(plaintext):
    """
    This is the registration link.
    """
    plaintext = plaintext.encode()
    encryption = encrypt(plaintext + secret)
    print("AES OUTPUT:")
    print_as_blocks(encryption)
    return encryption

def get_blocks(text):
    return [text[x:x+32] for x in range(0, len(text), 32)]

def print_as_blocks(text):
    for block in get_blocks(text):
        print(block)

if __name__ == "__main__":
    # We are going to write some code to do 1 Byte At A Time Decryption here.
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    while 1:
        register(input())
    # Now we start registering usernames that look like padded strings.
    # This will let us reveal 1 character at a time.
    

    pass
