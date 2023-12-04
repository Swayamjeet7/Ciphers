import numpy as np
from math import sqrt

def main():
    
    cipher = input("Enter the cipher text: ")
    length = len(cipher)
    key = input("Enter the key used for encryption: ")
    l = sqrt(len(key))
    
    key_matrix = []
    k = []
    n = 1
    
    for i,char in enumerate(key):
        k.append(ord(char) - 64)
        if i == l*n - 1:
            key_matrix.append(k)
            k = []
            n += 1

    cipher_matrix = []
    for char in cipher:    
        cipher_matrix.append(ord(char))

    key_inverse = np.linalg.inv(key_matrix)
    message_matrix = np.matmul(cipher_matrix, key_inverse)

    message = ""
    for n in range(length):
        symbol = str(chr(int(message_matrix[n] + 31)))
        message = message + symbol

    print(f"The message is: {message}")

if __name__ == "__main__":
    main()