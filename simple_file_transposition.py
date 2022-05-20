import math
import os
from tkinter import E

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
    print(os.getcwd())
    method = input("(E)ncryption or (D)ecryption? ")
    filename = input("Enter filename: ")
    key = int(input("Enter key length: "))


    filename = os.path.join(os.getcwd(), filename)
    with open(filename, 'r') as f:
        message = f.read()

    if method.lower() == 'e':
        with open(filename, 'wt') as f:
            f.write(encrypt_message(message, key))
    elif method.lower() == 'd':
        with open(filename, 'wt') as f:
            f.write(decrypt_message(message, key))

if __name__ == '__main__':
    main()