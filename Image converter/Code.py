#code to convert a coloured image to binary image
import cv2

def convert(input_path):
    img=cv2.imread(input_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,th = cv2.threshold(gray,150,255,0)
    zoom_factor=0.25
    z = cv2.resize(th, None, fx=zoom_factor, fy=zoom_factor, interpolation=cv2.INTER_LINEAR)
    return z
    
input_path="n.JPG"
binary_image=convert(input_path)
cv2.imshow("B",binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()