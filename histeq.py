import numpy
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('pout-dark.jpg',0)

hist=cv2.calcHist([img],[0],None,[256],[0,256])
histn=hist/hist.sum()
histn_cumulative=histn.cumsum()
hist_final_float=histn_cumulative*255
hist_final=hist_final_float.round()

img1=hist_final[img]
img1=img1.astype('uint8')

hist1=cv2.calcHist([img1],[0],None,[256],[0,256])

plt.plot(hist1)
plt.plot(hist)
plt.show()

cv2.imshow('equalized image',img1)
cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

