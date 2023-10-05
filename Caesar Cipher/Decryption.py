# This program is for decryption of a password 
password=input("Enter a password: ")
key=int(input("Enter the key used for encryption: "))
message=""
for char in password:
    if char==" ":
        msg=" "
    else:
        value=ord(char)
        new_value=value+key
        msg=chr(new_value)
    message=message+msg
print(message) 