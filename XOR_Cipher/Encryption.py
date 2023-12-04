def main():
    
    message = input("Enter a message: ")
    message = message.upper()
    message_code = ''.join(format(ord(char),'08b') for char in message)
    length = len(message_code)
    
    key = length*str(1)
    xor_value = ''.join('1' if bit1 != bit2 else '0' for bit1, bit2 in zip(message_code, key))
    cipher = ''.join(chr(int(xor_value[i:i+8], 2)) for i in range(0, len(xor_value), 8))
    
    print(f"The cipher text is: {cipher}")

if __name__ == '__main__':
    main()