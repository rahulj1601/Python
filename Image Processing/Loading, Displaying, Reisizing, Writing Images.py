import cv2

img = cv2.imread("galaxy.jpg", 0)
#pass 1 to read in colour
#pass 0 to read in grayscale
#-1 to read in colour with alpha channel (transparency operations)

print(type(img)) #image stores as a numpy array - matrix of numbers
print(img)
print(img.shape) #resolution of the image
print(img.ndim) #number of dimensions

###colour image has 3 dimensions for rgb
##img = cv2.imread("galaxy.jpg", 1)
##print(type(img)) 
##print(img)
##print(img.shape)
##print(img.ndim) 

resized_image = cv2.resize(img,(1000,500)) #resizes the image but doesn't maintain the same ratio of the dimensions - image appears distorted
ratio_resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) #resizes the dimensions maintaining the ratio of the image

cv2.imshow("Galaxy",ratio_resized_image) #displays the image and names the window - Galaxy

cv2.imwrite("Galaxy_resized.jpg",ratio_resized_image) #writes the image as a file

cv2.waitKey(0)
#0-when the user presses any button the window will close
#2000-milliseconds after which the window closes
cv2.destroyAllWindows() #closes all windows after key has been pressed for specific time
