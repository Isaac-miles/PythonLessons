#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACE_HOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as readNames:
    read_names = readNames.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in read_names:
        striped_name = name.strip()
        new_letter = letter_content.replace(PLACE_HOLDER, striped_name)
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}.docx","w") as completed_letter:
            completed_letter.write(new_letter)
