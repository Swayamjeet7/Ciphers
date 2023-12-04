import secrets

def main():
    
    text = input('Enter a message: ')

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz,.!?'
    length = len(text)
    
    otp = ''
    result = ''
    
    for i in range(length):
        
        otp += secrets.choice(letters)
        text_num = letters.find(text[i])
        key_num = letters.find(otp[i]) 
        
        if text_num == -1 :
            result = result + text[i]
        
        else:       
            result += letters[(text_num + key_num) % len(letters)]

    print(f'The OTP is: {otp}')
    print(f'The encrypted/decrypted text is: |{result}|')


if __name__ == '__main__':
    main()