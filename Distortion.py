import numpy as np
import cv2
import glob

#---------Calibrating Webcam using Python and OpenCV Error--------------#
# Below StackerOverflow reference was followed for this project
#https://stackoverflow.com/questions/31249037/calibrating-webcam-using-python-and-opencv-error?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

cbrow = 5
cbcol = 5

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((cbrow * cbcol, 3), np.float32)
objp[:, :2] = np.mgrid[0:cbcol, 0:cbrow].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('*.jpg')

#-------------- Camera Matrix Calculation------------#
# Calcaultes the camera specific properties for camera calibration as described
# in the stackoverflow post
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray,(cbrow,cbcol),None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (cbrow,cbcol), corners2,ret)
        cv2.imshow('img',img)
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
        #print(gray.shape[::-1])
       # print(imgpoints)
#--------------------------------------------------------------------#



#------------Undistorting the Image using the above calcualted camera matrix---#
# The undistortion happens two times. 'testImage' is first undistorted to produce
# a new image 'output_1'. Then 'output_1' is again undistorted to produce 
# 'finalUndistorted'.

# Motivation:
# Due to the fish eye lens being used by the team, it was identified after 
# multiple testing,that two undistortion were required to correctly undistort 
# the image

img = cv2.imread('testImage.png')
h,w = img.shape[:2]
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
cv2.imwrite('output_1.png',dst)
#cv2.imshow('imgafe',dst)

img = cv2.imread('output_1.png')
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
cv2.imwrite('finalUndistorted.png',dst)
#--------------------------------------------------------------------#
## crop the image
#x,y,w,h = roi
#dst = dst[y:y+h, x:x+w]


cv2.waitKey(500)
#cv2.destroyAllWindows()
