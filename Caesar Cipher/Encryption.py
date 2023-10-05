# This program is for encryption of a message using a key
message=input("Enter a message: ")
key=int(input("Enter a key value: "))
password=""
for char in message:
    if char==" ":
        ps=" "
    else:
        value=ord(char)
        new_value=value-key
        ps=chr(new_value)
    password=password+ps
print(password)  