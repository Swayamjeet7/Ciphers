import numpy as np

key_matrix = [[2,2,2]]

message=input("Enter a message: ")
message_matrix=[]
for char in message:
    m=[]
    m.append(ord(char))
    message_matrix.append(m)

cipher_matrix=np.multiply(key_matrix,message_matrix)
t=""
for num in range(len(message)):
    a=str(chr(cipher_matrix[num][0]))
    t=t+a
    
print(t)