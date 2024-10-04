import art
art.display_art()
alphabets= ["a","b","c","d","e","f","g","h","i","j",
            "k","l","m","n","o","p","q","r","s","t",
            "u","v","w","x","y","z","a","b","c","d","e",
            "f","g","h","i","j","k","l","m","n","o","p",
            "q","r","s","t","u","v","w","x","y","z"]
# print(len(alphabets))
direction= input("enter'encode' to encrypt or'decode'to decrypt: \n")
text= input("write a message: \n" ).lower()
shift= int(input("input your shift number: \n"))

def cipher(initial_text, shift_number, direction):
    end_text = ""
    if direction=='decode':
        shift_number*=-1
    for char in initial_text:
        if char in alphabets:
            position=alphabets .index(char)
            new_position= position + shift_number
            new_character=alphabets[new_position]
            end_text += new_character
        else:
            end_text+=char
    print(end_text)
cipher(initial_text=text, shift_number=shift, direction=direction)

# def encrypt (plain_text,shift_number):
#     encrypted_text = ""
#     for letter in plain_text:
#         position=alphabets .index(letter)
#         new_position= position + shift_number
#         new_character=alphabets[new_position]
#         encrypted_text += new_character
#     print(encrypted_text)



# def dencrypt (plain_text,shift_number):
#     dencrypted_text = ""
#     for letter in plain_text:
#         position=alphabets .index(letter)
#         new_position= position - shift_number
#         new_character=alphabets[new_position]
#         dencrypted_text += new_character
#     print(dencrypted_text)

# if direction=='encode':
#     encrypt (plain_text = text ,shift_number=shift )

# elif direction=='decode':
#     dencrypt (plain_text=text ,shift_number= shift)

# else:
#     print("invalid input")


