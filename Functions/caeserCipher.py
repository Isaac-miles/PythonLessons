"""ord('A'): Returns the ASCII value of 'A' (which is 65).

ord('Z'): Returns the ASCII value of 'Z' (which is 90).

chr(i): Converts the ASCII value back to its corresponding character.

List comprehension: Creates a list of characters from 'A' to 'Z'."""

alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]
alphabets.append(' ')
action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Enter the message you want to encrypt\n").lower()
shift = int(input("enter the number of shift\n"))

def encrypt_message(original_text,shift_amount):
    encrypted_text = ""
    for letter in original_text:
        shifted_position = alphabets.index(letter) +shift_amount
        shifted_position %= len(alphabets)
        encrypted_text += alphabets[shifted_position]
    print(encrypted_text)

encrypt_message(original_text=text,shift_amount=shift)

def decrypt_message(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        shifted_position = alphabets.index(letter) - shift_amount
        shifted_position %= len(alphabets)
        encrypted_text += alphabets[shifted_position]
    print(encrypted_text)

decrypt_message(original_text=text,shift_amount=shift)