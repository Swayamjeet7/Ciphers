def main():
    message = input('Enter a message: ')
    key = int(input('Enter a key number: '))
    
    cipher = [''] * key

    # Loop through each column in cipher:
    for column in range(key):
        index = column

        # Keep looping until index goes past the message length:
        while index < len(message):
            cipher[column] += message[index]

            index +=key

    # Print the cipher list by turning it into a single string 
    ciphertext = ''.join(cipher)
    print(ciphertext)

if __name__ == '__main__':
    main()