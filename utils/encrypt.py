from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend
import os
import json
import base64
import streamlit as st

def encrypt_file(input_path, output_path, password: str):
    # Load plaintext
    with open(input_path, 'rb') as f:
        plaintext = f.read()

    # Generate random salt
    salt = os.urandom(16)

    # Derive a key from the password
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=default_backend())
    key = kdf.derive(password.encode())

    # Encrypt using AES-GCM
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    # Save encrypted data + salt + nonce
    with open(output_path, 'wb') as f:
        f.write(salt + nonce + ciphertext)

    print(f"✅ Encrypted and saved to {output_path}")


def decrypt_file(input_path, output_path, password: str):
    with open(input_path, 'rb') as f:
        data = f.read()

    salt = data[:16]
    nonce = data[16:28]
    ciphertext = data[28:]

    # Re-derive the key
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=default_backend())
    key = kdf.derive(password.encode())

    # Decrypt
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)

    with open(output_path, 'wb') as f:
        f.write(plaintext)

