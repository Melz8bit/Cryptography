
from pydoc import plain


def encrypt_message(plaintext, key):
    ciphertext = [''] * key

    for column in range(key):
        index = column
        while index < len(plaintext):
            ciphertext[column] += plaintext[index]

            index += key

    return ''.join(ciphertext)
    

def main():
    plaintext = input("Enter plaintext: ")
    key = int(input("Enter key length: "))

    print(encrypt_message(plaintext, key))

if __name__ == '__main__':
    main()