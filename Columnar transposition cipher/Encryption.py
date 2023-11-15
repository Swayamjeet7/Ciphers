def encrypt(message,key):
    cipher = [''] * key

    # Loop through each column in cipher:
    for column in range(key):
        index = column

        # Keep looping until index goes past the message length:
        while index < len(message):
            cipher[column] += message[index]

            index +=key

    # Return the cipher list by turning it into a single string 
    return ''.join(cipher)   


def main():
    message = input()
    key = int(input())
    ciphertext = encrypt(message,key)
    print(ciphertext)

if __name__ == '__main__':
    main()