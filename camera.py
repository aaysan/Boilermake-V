import cv2

camera = cv2.VideoCapture(0)
def capture_image():
	# read is the easiest way to get a full image out of a VideoCapture object.
	retval, im = camera.read()
	return im

def main():
	for i in range(0,50):
	    temp = capture_image()
	    # Capture frame-by-frame
	capture = capture_image() 
	file1 = "barcode_01.jpg"
	cv2.imwrite(file1, capture)
	# del(camera)
