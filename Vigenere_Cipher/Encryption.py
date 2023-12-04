def main():
    
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    message = input('Enter a message: ')
    msg_length = len(message)
    msg = message.upper()

    key = input('Enter a key string: ')
    key_length = len(key)
    key = key.upper()

    keyindex = 0
    ciphertext = ''  # Stores the encrypted message string
    
    for i in range(0,msg_length) :
        msg_num = letters.find(msg[i])
        
        if msg_num == -1 :  # If msg[i] was not in letters
            ciphertext = ciphertext + msg[i]    # Add the symbol without encrypting
        
        else:       
            symbol = key[keyindex % key_length]
            key_num = letters.find(symbol) 
            keyindex += 1   # Move to the next letter in the key   
            
            ciphertext_num = (key_num + msg_num) % len(letters)  # Wrap-around of letters
                    
            # Add the encrypted letter to ciphertext
            if message[i].islower() :
                ciphertext = ciphertext + letters[ciphertext_num].lower()
            elif message[i].isupper() : 
                ciphertext = ciphertext + letters[ciphertext_num]   
    
    print(ciphertext)   

if __name__ == '__main__':
    main()