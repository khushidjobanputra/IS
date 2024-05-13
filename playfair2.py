def create_matrix(key, list1=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']):
    compElements,matrix = [],[]
    for i in key:
        if i not in compElements:
            compElements.append(i) 
    for i in list1:
        if i not in compElements:
            compElements.append(i)
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:] 
    return matrix

def addBuffer(message):
    index = 0
    while (index < len(message)-1):
        l1,l2 =message[index], message[index + 1]
        if l1 == l2:
            message = message[:index + 1] + "X" + message[index + 1:]
        index += 2
    if len(message)%2!=0:
        message+='X'
    return message

def indexOf(letter, matrix):
    for i in range(5):
        try:
            index = matrix[i].index(letter)
            return (i, index)
        except:
            continue

def playfair(key, message, encrypt=True):
    inc = 1 if encrypt else -1
    matrix = create_matrix(key)
    message = message.replace(' ', '')
    message = addBuffer(message)
    cipher_text = ''
    for (l1, l2) in zip(message[0::2], message[1::2]):
        row1, col1 = indexOf(l1, matrix)
        row2, col2 = indexOf(l2, matrix)
        if row1 == row2:
            cipher_text += matrix[row1][(col1 + inc) % 5] + matrix[row2][(col2 + inc) % 5]
        elif col1 == col2:
            cipher_text += matrix[(row1 + inc) % 5][col1] + matrix[(row2 + inc) % 5][col2]
        else:
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    return cipher_text

plainText = input("Enter the Plain text: ").upper()
key = input("Enter Key: ").upper().replace('J','I')
cipherText = playfair(key, plainText)
print(f'Encrypted:{cipherText}\nDecrypted:{playfair(key, cipherText, encrypt=False)}')