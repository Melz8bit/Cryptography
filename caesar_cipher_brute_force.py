import string

CHARACTERS = string.ascii_letters + string.digits + string.punctuation

user_input = input("Enter cipher: ")

for key in range(len(CHARACTERS)):
    translated = ''
    for character in user_input:
        index = CHARACTERS.index(character)
        
        new_index = index - key

        if new_index < 0:
            new_index += len(CHARACTERS)
            
        translated += CHARACTERS[new_index]

    print(f'Key {key}: {translated}')