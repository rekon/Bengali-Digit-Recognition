import cv2
import glob
import numpy as np
files = glob.glob('*\\*.tif')

kernel = np.ones((4,4),np.uint8)

for filepath in files:
    print('Processing file -',filepath)
    img = cv2.imread(filepath)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(filepath,img)
