import numpy
import cv2
import matplotlib.pyplot as plt

def find_nearest(array, value):
    array = numpy.asarray(array)
    idx = (numpy.abs(array - value)).argmin()
    return array[idx]

img=cv2.imread('pout-dark.jpg',0)
ref=cv2.imread('pout-bright.jpg',0)

hist=cv2.calcHist([img],[0],None,[256],[0,256])
hist_ref=cv2.calcHist([ref],[0],None,[256],[0,256])
histn=hist/hist.sum()
histn_ref=hist_ref/hist_ref.sum()
histn_cumulative=histn.cumsum()
histn_cumulative_ref=histn_ref.cumsum()
hist_final_float=histn_cumulative*255
hist_final_float_ref=histn_cumulative_ref*255
hist_final=hist_final_float.round()
hist_final_ref=hist_final_float_ref.round()

hist_final_sp=numpy.zeros(hist_final.shape)
for (x),value in numpy.ndenumerate(hist_final):
    hist_final_sp[x]=numpy.abs(hist_final_ref-hist_final[x]).argmin()

img1=hist_final_sp[img]
img1=img1.astype('uint8')
hist1=cv2.calcHist([img1],[0],None,[256],[0,256])
plt.plot(hist_final_sp,label='hist_final_sp')
plt.plot(hist_final,label='hist_final')
plt.plot(hist_final_ref,label='hist_final_ref')
plt.legend()
plt.show()

cv2.imshow('matched image',img1)
cv2.imshow('original image',img)
cv2.imshow('reference image',ref)
cv2.waitKey(0)
cv2.destroyAllWindows()
