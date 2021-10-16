# Drowsiness Detection System(web-app)

## Motivation: 
According to the National Highway Traffic Safety Administration, every year about 100,000 police-reported crashes involve drowsy driving. These crashes result in more than 1,550 fatalities and 71,000 injuries. The real number may be much higher, however, as it is difficult to determine whether a driver was drowsy at the time of a crash. So, we tried to build a system, that detects whether a person is drowsy and alert him.
This web-app is a one-page application for making it convenient and accessible to the user.

## Landing Page:
![image](https://user-images.githubusercontent.com/49195734/134022350-519e7522-0d02-4b90-95c3-678f2236b36f.png)

## Video Upload Button:
You need to enter the video link facing your face.
![image](https://user-images.githubusercontent.com/49195734/134024675-2eb7268e-94fc-492a-92f3-9d6bec1a531a.png)


## Working Details: 
The basic thing about drowsiness detection is pretty simple. We first detect a face using dlib's frontal face detector. Once the face is detected , we try to detect the facial landmarks in the face using the dlib's landmark predictor. The landmark predictor returns 68 (x, y) coordinates representing different regions of the face, namely - mouth, left eyebrow, right eyebrow, right eye, left eye, nose and jaw. Ofcourse, we don't need all the landmarks, here we need to extract only the eye and the mouth region. 

Now, after extraxting the landmarks we calculate the <b>Eye Aspect Ratio (EAR)</b> as: 

```python 
def eye_aspect_ratio(eye):
	# Vertical eye landmarks
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])
	# Horizontal eye landmarks 
	C = dist.euclidean(eye[0], eye[3])

	# The EAR Equation 
	EAR = (A + B) / (2.0 * C)
	return EAR
```
The eye region is marked by 6 coordinates. These coordinates can be used to find whether the eye is open or closed if the value of EAR is checked with a certain threshold value.<br>
![blink_detection_plot](https://user-images.githubusercontent.com/35571958/87878670-62d41400-ca03-11ea-8b96-fc4344c61a21.jpg)

In the same way I have calculated the aspect ratio for the mouth to detect if a person is yawning. Although, there is no specific metric for calculating this, so I have taken for points, 2 each from the upper and lower lip and calculated the mean distance between them as: 
```python 
def mouth_aspect_ratio(mouth): 
	A = dist.euclidean(mouth[13], mouth[19])
	B = dist.euclidean(mouth[14], mouth[18])
	C = dist.euclidean(mouth[15], mouth[17])

	MAR = (A + B + C) / 3.0
	return MAR
```
<b>Note: Learn more about dlib</b> <a href = "http://dlib.net/">here.</a>



### Future Scope: 
We are looking to convert this into an Android App which will be more portable and easily accessible. Also, we faced some issues while hosting this on Heroku. Any leads on these will be extremely helpful. 
