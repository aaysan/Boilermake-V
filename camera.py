import cv2

def capture_image(camera):
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im
def capture():
	camera = cv2.VideoCapture(0)
	'''
	while True:
	    ret_val, img = camera.read()
	    cv2.imshow('my webcam', img)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break
	cv2.destroyAllWindows()
	'''
	    # Capture frame-by-frame
	capture = capture_image(camera) 
	file1 = "pic1.jpeg"
	cv2.imwrite(file1, capture)
	del(camera)
