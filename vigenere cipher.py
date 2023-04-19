# Assignment 2 PROBLEM 3 The Vigenère Cipher
# Phoebe Rhone L. Gangoso | BSCPE 1-4

import pyfiglet
print("")
title_text = " This is The Vigenère Cipher "
title_line = title_text.center(150, "*")
print(title_line)
print("")

# ask the user to input message and key
input_message = input("\N{envelope} \033[0;35m Please enter your message: ")
input_key = input("\N{key} \033[0;33m What is your key?: ")
# convert message and key to uppercase letters
input_message = input_message.upper()
input_key = input_key.upper()

print("")
# loading animation
import time
for i in range(3):
    print("\033[0;34m Generating your Ciphertext", end="\N{slightly smiling face}")
    for j in range(4):
        print(".", end="")
        time.sleep(0.25)
    print("\r", end="")
print("DONE!\N{grinning face}")

# create a function to encrypt the message
def vigenere_cipher(input_message, input_key):
    cipher_text = ""
    key_index = 0

#   iterate every character in the message
    for char in input_message:
#       if character is an alphabet, encrypt with key character
        if char.isalpha():
            key_char = input_key[key_index % len(input_key)]
            message_code = ord(key_char.lower()) - 97
            if char.isupper():
                cipher_text += chr((ord(char) - 65 + message_code) % 26 + 65)
            else:
                cipher_text += chr((ord(char) - 97 + message_code) % 26 + 97)
            key_index += 1
#       if character is not an alphabet, append as it is
        else:
            cipher_text += char
#   return encrypted message
    return cipher_text

# encrypt message with key using the function
cipher_text = vigenere_cipher(input_message, input_key)
print("")
# print output ciphertext
print("\N{ribbon}\N{ribbon}\N{ribbon} \033[0;32m Here is the Ciphertext: \N{ribbon}\N{ribbon}\N{ribbon} ")
print("")
print("\033[0;36;40m")
print(pyfiglet.figlet_format(cipher_text, font = "basic", width = 150))