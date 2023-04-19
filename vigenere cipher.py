# Assignment 2 PROBLEM 3 The Vigenère Cipher
# Phoebe Rhone L. Gangoso | BSCPE 1-4

#PSEUDOCODE

# ask the user to input message and key
input_message = input("Please enter your message: ")
input_key = input("What is your key?: ")
# convert message and key to uppercase letters
input_message = input_message.upper()
input_key = input_key.upper()

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
ciphertext = vigenere_cipher(input_message, input_key)
# print output ciphertext
print("Here is the Ciphertext:", ciphertext)