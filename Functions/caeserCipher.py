"""ord('A'): Returns the ASCII value of 'A' (which is 65).

ord('Z'): Returns the ASCII value of 'Z' (which is 90).

chr(i): Converts the ASCII value back to its corresponding character.

List comprehension: Creates a list of characters from 'A' to 'Z'."""

alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]

def caesar(original_text,shift_amount,encode_or_decode):
    """This encode and decodes the input based on the user's prompt"""
    encrypted_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        #when a user enters special char or space
        if letter not in alphabets:
            encrypted_text += letter
        else:
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position %= len(alphabets)
            encrypted_text += alphabets[shifted_position]
    print(f"{encode_or_decode}d is {encrypted_text}")

should_continue = True

while should_continue:
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Enter the message you want to encrypt\n").lower()
    shift = int(input("enter the number of shift\n"))

    caesar(original_text=text,shift_amount=shift,encode_or_decode=action)

    restart = input("Type 'yes' if you want to go again. Otherwise,type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Good bye")
