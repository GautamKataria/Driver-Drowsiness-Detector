# Eye-Based-Driver-Drowsiness-Detector

## This Repository hosts the code and files required to perform driver drowsiness detector with the help of cnn classification.

## To Run:

### Copy python file in working directory.
### Copy weights file in working directory.
### Run the eye_driver_detect.py file.
### link to weights for eye based model: [Here](https://drive.google.com/file/d/1Lr8WcUxcZ4cYR6B932vZX0zCZNmKNot2/view?usp=sharing)

### Theoretical working:
Step1: The program activated the camera and starts the process of capturing frames.

Step2: We change the coloured image to grayscale to make the detection more accurate and reliable. The program then detects the drivers’ eyes using an eye based haarcascade (haarcascade_lefteye_2splits.xml) which is then shown to the user as a bounding box around the eyes.

Step3: Further we crop out this detected region of interest (ROI), which would be a cut-out of the eye region which is also shown in a separate window to the user.

Step4: Then our trained model takes in the grayscale eye ROI image as input and classifies it into focused or drowsy (eyes opened or closed). 
After detection and classification, we can perform any action desired. In this case we are just adding the classified class on the user window.
