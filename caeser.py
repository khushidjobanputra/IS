def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if char.isupper() else 'abcdefghijklmnopqrstuvwxyz'
            shifted = (alphabet.index(char) + shift) % 26
            result += alphabet[shifted]
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Example usage
text = "vxevwlwxwlrq Flskhu"
shift = 3
encrypted_text = caesar_encrypt(text, shift)
decrypted_text = caesar_decrypt(encrypted_text, shift)

print("Original text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)