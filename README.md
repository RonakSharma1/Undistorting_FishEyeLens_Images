# Aim
This algorithm undistorts the images captured using a fish eyed lens camera. 

# Motivation
This algorithm was developed for [MATE ROV International Competition 2017/18](https://materovcompetition.org/).The mission was to place an object at a specified distance from a reference object provided by the judges. Since the team only had access to fish eyed lens camera, hence the image captured of the reference object was first undistorted using this software. Using this undistorted image and the reference object, further calculations were performed to determine the location where the object had to be placed. These calculations would have been incorrect if the distorted image was used instead thus leading to the object placement at the wrong location.

# Structure of Folder
1. 'Distortion.py': Main algorithm
2. 'common.py': Module required to run the above file
3. '1-10.jpg': All '.jpg' images were used for computing the camera matrix(i.e. camera parameters). These were captured using fish eye camera 
4. '1 .png': A single '.png' image was used as a test image for undistoring(testing). This was captured using fish eye camera as well


# Setup/Installation
```
sudo apt-get install opencv-python
```
1. Clone all the images attached in this repository i.e. ten '.jpg' files and one testimage i.e. a '.png' file
2. Run 'Distortion.py' for undistorting the 'testimage.png'
3. Two images will be generated and final undistorted image will be stored as 'finalUndistored.png'

# Results
## Comparing the Distorted and Undistorted Image
### Distorted Image
![testImage](https://user-images.githubusercontent.com/34181525/82432006-5412c480-9a87-11ea-887c-80109bfe9b13.png)

### Undistorted Image
![finalUndistorted](https://user-images.githubusercontent.com/34181525/82431996-5117d400-9a87-11ea-98f1-ecde71e9cbeb.png)

1. To verify the result, the distance shown by the vernier calliper i.e. 70.6cm was measured using the software developed in repository "Distance_Measurement".This software calcaultes the distance between any two points (in this case b/w the ends of the vernier calliper) and then compares it to the actual distance between those two points.
2. Applying the above software on the undistorted image, the distance came out be 70.7cm as compared to 70.6cm , thus showing high accuracy
3. This algorithm was then tested with various other orientations and distances b/w the calliper ends. Overall, the algorithm showed good performance with an error of +/- 0.01% only.

# Modifications for Wider Community Usage
1. As explained earlier, all the '.jpg' files were captured using the fish eye camera and were used to compute some camera specific parameters/properties. The undistortion algorithm was then applied to the 'testimage.png' 
2. To use this algorithm for undistorting your image, capture a minimum of ten images of a Black and White chessboard and store these images as '.jpg' files. In the same folder with the name of 'testimage.png', store the image you would like to undistort. Then follow the steps described in 'Setup/Installation'


# General
1. To solve my problem efficiently, I had to undistort the image twice. Multiple tests were performed to compare a single undistorted and twice undistorted image and the latter was found to perform significantly better
