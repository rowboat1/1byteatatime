import aes
import os
import time
import base64

key = os.urandom(16)

# Your goal is to use main.py to figure out what this secret is.

# You might already know how to decode base64, but don't do it directly!
# This is about decrypting AES (what if you didn't have access to this secret?)
secret = base64.b64decode(
    "UGxlYXNlIGJybywgSSBiZWdnZWQgeW91IG5vdCB0byBkZWNvZGUgbGlrZSB0a" +
    "GlzISBZb3Ugc2hvdWxkbid0IGZlZWwgaGFwcHkgYWJvdXQgdGhpcywgYnV0IH" + 
    "RoZSBzb2x1dGlvbiBpczogcmljZXBhcGVycm9sbA=="
)[-14:]

def pad(text):
    if type(text) == bytes:
        return text + b"_" * (16 - len(text)%16)
    else:
        return text + "_" * (16 - len(text)%16)

def show_plaintext_blocks(plaintext):
    # Remember how you promised not to print(secret) before the class
    output = plaintext.replace(secret, b"*" * len(secret))
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
    blocks = get_blocks(encryption)
    return encryption, blocks

def get_blocks(text):
    return [text[x:x+32] for x in range(0, len(text), 32)]
