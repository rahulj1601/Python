import cv2, glob, os

imgDirectory = "/Users/rahul/Documents/Programming/The Python Mega Course/Image and Video Processing/images/"

os.chdir(imgDirectory)
images = glob.glob("*.jpg")

os.chdir("/Users/rahul/Documents/Programming/The Python Mega Course/Image and Video Processing/")

for i in images:
    image = imgDirectory + i
    img = cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Image",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+i,re)
