# The Luca Bazooka

##Summary
This is a project started in the Robotics-Mechatronics class at Nueva High School. In order to support LBPH Histograms, OpenCV3 with opencv-contrib or OpenCV2 is required along with imageio and (optionally) skimage for additional visualization.

##Files 'n Stuff
pi-recognize.py: Code made to run on the Raspberry Pi that detects faces inputed into the training folder 

pi-detect.py: Detects any sort of face using Haar Cascades (cascade data pulled from opencv) 

testable-recognize.py: Nearly identical code to pi-recognize but configured so it can be run on a computer 

servo.py: Contains the servo class used to point the laser pointer at a given coordinate. Used exclusively with the pi python code

##Dev Path (Ethan/hyperdo)
 - Finalize OpenCV code for mac
 - Write Servo code for RasPi
 - Development moves entirely to Raspberry (we all collectively pray) 
 - Tyler Kant takes away our Raspberry Pi and dreams (thanks Tyler)
 - Track down Tyler in English class multiple times
 - Luca breaks first raspberry pi while trying to get into stolen RasPi, have to get new, worse pi (thanks Luca)
 - Spend multiple class periods lamenting over loss of raspberry pi and trying to fix anything if possible
 - Try to get OpenCV installed on RasPi - eventually settle on installing libopencv using apt-get after two-three weeks
   + https://stackoverflow.com/questions/34983116/opencv-face-recognition-in-python
   + https://stackoverflow.com/questions/35724372/manually-selecting-apt-get-install-opencv2
 - Debugged servo code for RasPi
 - Watched RasPi twitch in terror after seeing Luca (problem not yet resolved)
 - Fine-tune servo params
 - Try to get servos set up on RasPi but use wrong I/O pins, eventually use random pins
 - Change opencv capture and reconfig pi-recognize to use propreitary pi camera module
 - Debug servo code again, this time using oscilloscope
 - Added more training images
 - Changed one of the servo to one with wires that look like Germany
   + Also known as changing continuous motion servo to one that has limits
 - Added even more training images, reverted when Luca's face stopped being a face
 - Started development on coil gun
 - Coil gun renamed to ferro-magnetic object launching device

