import math

def decrypt_message(ciphertext: str, key):
    dec_key = math.ceil(len(ciphertext) / key)
    plaintext = [''] * dec_key

    shaded_boxes = (key * dec_key) - len(ciphertext)

    column = 0
    row = 0

    for character in ciphertext:
        plaintext[column] += character
        column += 1

        if column == dec_key or (column == dec_key - 1 and row >= key - shaded_boxes):
            column = 0
            row += 1
    
    return ''.join(plaintext)

def encrypt_message(plaintext, key):
    ciphertext = [''] * key

    for column in range(key):
        index = column
        while index < len(plaintext):
            ciphertext[column] += plaintext[index]

            index += key

    return ''.join(ciphertext)    

def main():
    method = input("(E)ncryption or (D)ecryption? ")
    text = input("Enter message: ")
    key = int(input("Enter key length: "))

    if method.lower() == 'e':
        print(f'{encrypt_message(text, key)}|')
    elif method.lower() == 'd':
        print(decrypt_message(text, key))


if __name__ == '__main__':
    main()