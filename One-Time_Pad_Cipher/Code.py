import secrets

def convert(text,mode):
    
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz,.!?'
    length = len(text)

    otp = ''
    if mode == 'e':
        otp += secrets.choice(letters)

    if mode == 'd':
        otp = input('Enter the OTP: ')

    result = ''
    for i in range(length):
        
        text_num = letters.find(text[i])
        key_num = letters.find(otp[i]) 
        
        if text_num == -1 :
            result = result + text[i]
        
        elif mode == 'e':       
            result += letters[(text_num + key_num) % len(letters)]
        
        elif mode == 'd':
            result += letters[(text_num - key_num) % len(letters)]

    return otp,result

def main():
    
    text = input('Enter a message/ciphertext: ')
    mode = input('Do you want to encrypt(e) or decrypt(d): ')
    otp,result = convert(text,mode)
    print(f'The OTP is: {otp}')
    print(f'The encrypted/decrypted text is: |{result}|')


if __name__ == '__main__':
    main()