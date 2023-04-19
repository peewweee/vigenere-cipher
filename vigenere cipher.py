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
#   iterate every character in the message
#       if character is an alphabet, encrypt with key character
#       if character is not an alphabet, append as it is
#   return encrypted message

# encrypt message with key using the function
# print output ciphertext