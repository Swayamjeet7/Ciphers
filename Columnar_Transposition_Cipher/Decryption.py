from math import ceil

def main():
    message = input('Enter the ciphertext: ')
    key = int(input('Enter the key used for encryption: '))

    # shape of transposition grid
    numofRows = key
    numofColumns = int(ceil(len(message) / float(key))) 
    emptySpace = numofRows * numofColumns - len(message)

    text = [''] * numofColumns

    # initialization
    row = 0
    column = 0
    
    for char in message:
        text[column] += char
        column += 1 

        # If there are no more columns OR position is at an emptySpace, 
        # go back to the first column and the next row
        if (column == numofColumns) or (column == numofColumns - 1 and row >= numofRows - emptySpace):
            column = 0
            row += 1

    message = ''.join(text)
    print(message)

if __name__ == '__main__':
    main()