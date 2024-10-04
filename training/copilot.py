alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
             "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e",
             "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
             "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Enter 'encode' to encrypt or 'decode' to decrypt: \n")
text = input("Write a message: \n").lower()
shift = int(input("Input your shift number: \n"))

def encrypt(plain_text, shift_number):
    encrypted_text = ""
    for letter in plain_text:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = position + shift_number
            new_character = alphabets[new_position]
            encrypted_text += new_character
        else:
            encrypted_text += letter
    print(f"Encrypted message: {encrypted_text}")

def decrypt(cipher_text, shift_number):
    decrypted_text = ""
    for letter in cipher_text:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = position - shift_number
            new_character = alphabets[new_position]
            decrypted_text += new_character
        else:
            decrypted_text += letter
    print(f"Decrypted message: {decrypted_text}")

if direction == 'encode':
    encrypt(plain_text=text, shift_number=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_number=shift)
else:
    print("Invalid input")