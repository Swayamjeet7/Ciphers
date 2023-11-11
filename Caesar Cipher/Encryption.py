# This program is for encryption of a message using a key
# In this code the ASCII values considered are from 32('SPACE') to 126('~')

message=input("Enter a message: ")
key=int(input("Enter a key value: "))
password=""

for char in message:
    value =  ord(char)
    key = key % 126
    new_value = value + key 
    
    if new_value > 126 :
        new_value = (new_value % 126) + 31
    
    ps = chr(new_value)
    password = password+ps
print(password)  