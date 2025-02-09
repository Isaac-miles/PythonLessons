"""ord('A'): Returns the ASCII value of 'A' (which is 65).

ord('Z'): Returns the ASCII value of 'Z' (which is 90).

chr(i): Converts the ASCII value back to its corresponding character.

List comprehension: Creates a list of characters from 'A' to 'Z'."""

alphabets = [chr(i) for i in range(ord('A'), ord('Z')+1)]

action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Enter the message you want to encrypt\n")
shift = int(input("enter the number of shift\n"))

encrypted_text =""
def encrypt_message(original_text,shift_amount):
    for letter in original_text:
        shifted_position = alphabets.index(letter)+ shift
        shifted_position %= len(alphabets)
        cipher_text = alphabets[shifted_position]