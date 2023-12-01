#from Encryption import cipher

def decryption(cipher):
    cipher_code=''.join(format(ord(char),'08b') for char in cipher)
    length=len(cipher_code)
    key=length*str(1)
    xor_value=''.join('1' if bit1 != bit2 else '0' for bit1, bit2 in zip(cipher_code, key))
    message=''.join(chr(int(xor_value[i:i+8], 2)) for i in range(0, len(xor_value), 8))
    return message

cipher=input("Enter the cipher: ")
message = decryption(cipher)
print(message)