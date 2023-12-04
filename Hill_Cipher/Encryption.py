import numpy as np

def key_generator(ln):
    
    for i in range(10):
        key_matrix = np.random.randint(5, size=(ln,ln))
        if np.linalg.det(key_matrix) != 0 :
            break
    
    key_text=""
    
    for m in range(ln):
        for n in range(ln):
            key_text = key_text + chr(key_matrix[m][n] + 64)
    
    return key_matrix,key_text


def main():
    message = input("Enter a message: ")
    length = len(message)
    message_matrix = []
    
    for char in message:
        message_matrix.append(ord(char) - 31)

    key,key_text = key_generator(length)

    cipher_matrix = np.matmul(message_matrix, key)   

    cipher = ""
    for n in range(length):
        symbol = str(chr(cipher_matrix[n] ))
        cipher = cipher+symbol

    print(f"The cipher is: {cipher}")
    print(f"The key used for encryption is: {key_text}")

if __name__ == "__main__":
    main()