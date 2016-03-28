




import RPi.GPIO as GPIO
import servo
servo = servo.Servo(8,10,53.5/640, 41.41/480, 640, 480)
servo.write_horizon(100)
GPIO.cleanup()
