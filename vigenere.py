def vigenere(plain_text, key, encrypt=True):
    result = ""
    key_index = 0
    factor = 1 if encrypt else -1

    for char in plain_text:
        if char.isalpha():
            char = char.upper()
            key_char = key[key_index % len(key)].upper()
            encrypted_char = chr(((ord(char) + factor * ord(key_char) - 2 * ord('A')) % 26) + ord('A'))
            key_index += 1
            result += encrypted_char
        else:
            result += char
    
    return result

plain_text = str(input("Enter string: "))
key = str(input("Enter key: "))
cipher_text = vigenere(plain_text, key)
decrypted_text = vigenere(cipher_text, key, encrypt=False)
print("Encrypted:", cipher_text)
print("Decrypted:", decrypted_text)