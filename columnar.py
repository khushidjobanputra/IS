import math

pt = input("Enter the plaintext : ").upper()
key = input("Enter the key : ").upper()

def find_rank(key):
    rank = 0
    for i in sorted(key):
        key = key.replace(i, str(rank), 1)
        rank += 1
    key = [int(i) for i in key]
    return key

def encrypt(pt, key):
    cols = len(key)
    rows = math.ceil(len(pt) / cols)
    key_rank = find_rank(key)
    print(key_rank)
    pt += "".join(["X"] * (rows * cols - len(pt)))
    matrix = [list(pt[i : i + cols]) for i in range(0, len(pt), cols)]
    for i in range(rows):
        print(matrix[i])
    ciphertext = ["*" for i in range(cols)]
    j = 0
    for i in key_rank:
        ciphertext[i] = [row[j] for row in matrix]
        j += 1
    res = []
    for i in ciphertext:
        res.extend(i)
    return "".join(res)


def decrypt(cip, key):
    cols = len(key)
    rows = math.ceil(len(cip) / cols)
    key_rank = find_rank(key)
    cip += "".join(["X"] * (rows * cols - len(cip)))
    cip_mat  = [list(cip[i:i+rows]) for i in range(0, len(cip), rows)]
    res = []
    for i in range(rows):
        a = ["*"] *(len(key_rank))
        count = 0
        for r in key_rank:
            a[count] = cip_mat[r][i]
            count +=1
        res.extend(a)
    return "".join(res).rstrip("X")


print(f"\nPlain text : {pt}\nKey:{key}\n")
ciphertext = encrypt(pt, key)
print(f"After encryption, Cipher Text : {ciphertext}\n")
decrypted_text = decrypt(ciphertext, key)
print(f"After decryption, Plain Text : {decrypted_text}")