'''
Also a test file for the servo class, similar to test.py
'''
import RPi.GPIO as GPIO
import servo,time
servo = servo.Servo(12,23,53.5/640, 41.41/480, 640, 480,90,90)
print('sleep ended')
for i in range (0,10):
    servo.update(200,300)
#time.sleep(2)
#GPIO.cleanup()
