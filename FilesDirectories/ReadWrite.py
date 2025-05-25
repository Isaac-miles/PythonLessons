
with open("my_file.txt") as file:
    content = file.read()
    print(content)

with open("my_file.txt","a") as file:
    file.write("\nhello miles dolce")