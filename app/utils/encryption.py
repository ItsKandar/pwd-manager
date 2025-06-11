from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import hashlib

def encrypt(password: str, key: str) -> bytes:
    key_hash = hashlib.sha256(key.encode()).digest()
    cipher = AES.new(key_hash, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(password.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext)

def decrypt(encrypted: bytes, key: str) -> str:
    encrypted = base64.b64decode(encrypted)
    nonce, tag, ciphertext = encrypted[:16], encrypted[16:32], encrypted[32:]
    key_hash = hashlib.sha256(key.encode()).digest()
    cipher = AES.new(key_hash, AES.MODE_EAX, nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()