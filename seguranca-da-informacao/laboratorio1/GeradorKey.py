from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# Gerar chave AES de 128 bits
key = AESGCM.generate_key(bit_length=128)

# Gerar nonce (12 bytes é o padrão recomendado para AESGCM)
nonce = os.urandom(12)

print("Key:", key)
print("Nonce:", nonce)

# Key: b'A\xe0 9.\xd6\x1cNY\xba\xf7\x08d\xa9To'
# Nonce: b'\x95\xa4\xad#\xceg\xbd\x02w\x8cf\x05'