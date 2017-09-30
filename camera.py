import cv2

camera = cv2.VideoCapture(0)
def capture_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 
 return im
c = True
  
    

while c == True:
    ret_val, img = camera.read()
        
    cv2.imshow('my webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        c = False
        break
temp = capture_image()
        
cv2.destroyAllWindows()
    # Capture frame-by-frame
capture = capture_image() 
file1 = "pic1.jpeg"
cv2.imwrite(file1, capture)
del(camera)
