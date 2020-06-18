# Aim
This algorithm undistorts the images captured using a fish eyed lens camera. 

# Motivation
This algorithm was developed for [MATE ROV International Competition 2017/18](https://materovcompetition.org/).The mission was to place an object at a specified distance from the reference point. Since the team only had access to fish eye lens camera, hence the image captured of the reference point was first undistorted using this software. Then using the reference, further calculations were performed to identify the location of object placement. These calculations would have been incorrect if the distorted image would have been used instead.

# Structure of Folder
1. Main Proposed Algorithm: 'Distortion.py'
2. Module required to run the above file:'common.py'
3. 10 '.jpg' images for computing camera matrix. These were captured using fish eye camera 
4. 1 .png image for undistoring(testing). This was captured using fish eye camera 


# Setup/Installation
1. sudo apt-get install opencv-python
2. Clone all the images attached in this repository i.e. ten '.jpg' files and one testimage i.e. a '.png' file
3. Run 'Distortion.py' for undistorting the 'testimage.png'
4. Two images will be generated and final undistorted image will be stored as 'finalUndistored.png'

# Results
## Comparing the Distorted and Undistorted Image
### Distorted Image
![testImage](https://user-images.githubusercontent.com/34181525/82432006-5412c480-9a87-11ea-887c-80109bfe9b13.png)

### Undistorted Image
![finalUndistorted](https://user-images.githubusercontent.com/34181525/82431996-5117d400-9a87-11ea-98f1-ecde71e9cbeb.png)

To verify the results, the distance shown by the vernier calliper i.e. 70.6cm was measured using the software created in repository XXXXXX. The distance came out be 70.7cm , thus showing the accuracy of this algorithm. This algorithm was tested with various orientation and distances b/w the calliper ends. The algorithm showed good performance with an error of +/- 0.01% only.

# Modifications for Wider Community Usage
As explained earlier, all the '.jpg' files were captured using the fish eye camera and were used to compute some camera specific properties. And the 'testimage.png' was used to apply the undistortion algorithm.

To use this algorithm for undistorting your image, capture a minimum of ten images of a B/W chessboard and store them as '.jpg' files. In the same folder with the name of 'testimage.png', store the image you would like to undistort. Then follow the steps described in 'SetUp/Installation'


# Note
1. To solve my problem efficiently, I had to undistort the image twice. Multiple tests were performed to compare a single undistorted and twice undistorted image and the latter was found to perform significantly better
2. For testing described in Point 1, the algorithm developed in repository XXXXXXX can be referred. This algorithm calculated the distance between the ends of the vernier calliper and compared it to the actual distance between those two ends.
