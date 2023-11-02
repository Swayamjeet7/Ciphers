from PIL import Image

def encrypt(image_path,text):
    # Converts the text into binary
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    
    img=Image.open(image_path)
    
    pixels = img.load()
    index = 0
    for i in range(img.width):
	    for j in range(img.height):
              r, g, b =pixels[i,j]
              
              # Modifies the least significant bit 
              if index < len(binary_text):
                  r=(r & 0xFE) | int(binary_text[index])
                  index += 1
              if index < len(binary_text):
                  g=(g & 0xFE) | int(binary_text[index])
                  index += 1  
              if index < len(binary_text):
                  b=(b & 0xFE) | int(binary_text[index])
                  index += 1  

              pixels[i,j] = (r,g,b) 

    return img         


def main():
    image_path=input("Enter image path: ")
    text=input("Enter the text: ")
    output_path=input("Enter output path: ")
    new_image = encrypt(image_path,text)
    new_image.save(output_path)

if __name__=="__main__":
    main()