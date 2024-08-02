import string
def encrypt(message, shift):
    alphabet = string.ascii_lowercase
    encrypted_message = ""
    for letter in message:
        if letter.lower() in  alphabet:
            origianl_position = alphabet.index(letter.lower())
            new_position = (origianl_position - shift) % 26
            encrypted_letter = alphabet[new_position]
            if letter.isupper():
                encrypted_letter = encrypted_letter.upper()

            encrypted_message += encrypted_letter
        else:
            encrypted_message += letter
    print (encrypted_message)

a = input("enter a message: ")
b = int (input("enter a shift num: "))


encrypt(message=a , shift=b)
