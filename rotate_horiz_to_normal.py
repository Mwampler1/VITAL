


import cv2
 
# read image as grey scale
img = cv2.imread('/home/rtp/rtp/Heatmap-Processing/horizontalpic.png')
# get image height, width
(h, w) = img.shape[:2
                    ]
# calculate the center of the image
center = (w / 2, h / 2)
 
angle90 = 90
 
scale = 1.0
 
# Perform the counter clockwise rotation holding at the center
# 90 degrees
M = cv2.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv2.warpAffine(img, M, (h, w))

#show image
cv2.imshow('Rotated Image', rotated90)
cv2.waitKey(0) # waits until 0 key is pressed
cv2.destroyAllWindows()
