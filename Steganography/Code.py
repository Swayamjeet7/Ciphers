from PIL import Image

def encrypt(image_path,text):
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    img=Image.open(image_path)
    img_size=img.height*img.width*3
    if img_size < len(binary_text):
        raise ValueError("Text is much larger")
    
    pixels=img.load()
    index=0
    for i in range(img.width):
	    for j in range(img.height):
              r, g, b =pixels[i,j]
              
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
    image_path=input("Image path: ")
    text=input("Text: ")
    output_path=input("Output path: ")
    new_image = encrypt(image_path,text)
    new_image.save(output_path)

if __name__=="__main__":
    main()