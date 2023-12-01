# This program is for decryption of the encrypted message 

def code():
    password=input("Enter the encrypted message: ")
    key=int(input("Enter the key used for encryption: "))
    message=""

    for char in password:
        key = key % 126
        value=ord(char)
        new_value=value-key
    
        if new_value <= 31 :
            new_value = 126 - (31 - new_value)
    
        msg=chr(new_value)
        message=message+msg
    print(message) 

if __name__ == '__main__': 
    code()   