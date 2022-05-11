import string

CHARACTERS = string.ascii_letters + string.digits + string.punctuation

user_input = input("Enter text: ")
method = ''

while method != 'e' and method != 'd':
    method = input("Is this an (E)ncryption or (D)ecryption? ").lower()

key = int(input("What is the key? "))

translated = ''
for character in user_input:
    if character in CHARACTERS:
        index = CHARACTERS.index(character)
        
        new_index = 0
        if method == 'e':
            new_index = index + key

            if new_index >= len(CHARACTERS):
                new_index -= len(CHARACTERS)
        
        else:
            new_index = index - key

            if new_index < 0:
                new_index += len(CHARACTERS)
    else:
        translated += character
            
    translated += CHARACTERS[new_index]

print(translated)