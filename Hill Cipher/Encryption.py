import numpy as np

message=input("Enter a message: ")
length=len(message)

message_matrix=[]
for char in message:
    m=[]
    m.append(ord(char) - 31)
    message_matrix.append(m)

key = np.random.randint(5, size=(length,length))

cipher_matrix=np.multiply(message_matrix, key)   

cipher=""
for n in range(length):
    symbol=str(chr(cipher_matrix[n][0]))
    cipher=cipher+symbol


print("The cipher is: ")
print(cipher)