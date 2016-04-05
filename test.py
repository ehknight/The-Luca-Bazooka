'''
File for testing whether the main servo class is working
'''

import RPi.GPIO as GPIO
import servo
servo = servo.Servo(8,10,53.5/640, 41.41/480, 640, 480) #Simply tells the servo on pins 8 and 10 to rotate, giving it the size and resolution of the camera
servo.write_horizon(100)
GPIO.cleanup()
