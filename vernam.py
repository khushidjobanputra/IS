def vernam_encrypt(plaintext, key):
    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]  # Repeat the key if it's shorter than the plaintext
    ciphertext = ""
    for p, k in zip(plaintext, key):
        p_val = ord(p.lower()) - ord('a')
        k_val = ord(k.lower()) - ord('a')
        xor_val = (p_val + k_val) % 26
        ciphertext += chr(xor_val + ord('a'))
    return ciphertext

def vernam_decrypt(ciphertext, key):
    key = key * (len(ciphertext) // len(key)) + key[:len(ciphertext) % len(key)]  # Repeat the key if it's shorter than the ciphertext
    plaintext = ""
    for c, k in zip(ciphertext, key):
        c_val = ord(c.lower()) - ord('a')
        k_val = ord(k.lower()) - ord('a')
        xor_val = (c_val - k_val) % 26
        plaintext += chr(xor_val + ord('a'))
    return plaintext

plaintext = str(input("Enter string: "))
key = str(input("Enter key: "))
ciphertext = vernam_encrypt(plaintext, key)
decrypted_text = vernam_decrypt(ciphertext, key)
print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)