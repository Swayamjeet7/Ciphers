def cases(opt1,opt2):

    match(opt1,opt2):
        
        case '1','1':
            from Caesar_Cipher import Encryption
            Encryption.code()
        
        case '1','2':    
            from Caesar_Cipher import Decryption
            Decryption.code()
        
        case '2','1':
            from Columnar_Transposition_Cipher import Encryption 
            Encryption.main()                        
        
        case '2','2':
            from Columnar_Transposition_Cipher import Decryption 
            Decryption.main()

        case '3','1':
            from Vigenere_Cipher import Encryption
            Encryption.main()

        case '4','1':
            from XOR_Cipher import Encryption
            Encryption.main()

        case '4','1':
            from XOR_Cipher import Decryption
            Decryption.main()

        case '5','1':
            from Hill_Cipher import Encryption
            Encryption.main()

        case '5','2':
            from Hill_Cipher import Decryption
            Decryption.main()

        case '6','1':
            from One_Time_Pad_Cipher import Encryption
            Encryption.main()

        case '6','2':
            from One_Time_Pad_Cipher import Decryption
            Decryption.main()    

        
def code():
    """    
Made by Swayamjeet
    
This a python program for the purpose of 
encryption and decryption of any message.\n
"""
    print(r"""       ____  _         _                      
      / ___|(_) _ __  | |__    ___  _ __  ___ 
     | |    | || '_ \ | '_ \  / _ \| '__|/ __|
     | |___ | || |_) || | | ||  __/| |   \__ \
      \____||_|| .__/ |_| |_| \___||_|   |___/
               |_| 
          """)

    print(code.__doc__ )
    
    option1 = input('''Which cipher do you want to use ?
    (1) Caesar cipher
    (2) Columnar transposition cipher
    (3) Vignere cipher
    (4) XOR cipher
    (5) Hill cipher
    (6) One Time Pad cipher \n
>> ''')
    
    option2 = input('''What do you want to do ?
    (1) Encryption
    (2) Decryption
>> ''')
    
    try:
        cases(option1,option2)
    except:
        print('Some error occurred !')    
    
if __name__ == "__main__" :
    code()          