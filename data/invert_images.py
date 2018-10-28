import cv2
import glob
files = glob.glob('*\\*.tif')

for filepath in files:
    img = cv2.imread(filepath)
    img = 255.0 - img
    path,ext = filepath.split('.')
    filepath = path + '_inv.' + ext
    cv2.imwrite(filepath,img)