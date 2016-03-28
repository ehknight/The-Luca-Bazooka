import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21,GPIO.OUT)
servo = GPIO.PWM(21,100)
servo.start(10)
while True:
    servo.ChangeDutyCycle(20)


#try:
 #   for i in range(0,100):
  #      servo.ChangeDutyCycle(i/10)
   #     time.sleep(0.01)

#except KeyboardInterrupt:
#    servo.stop()
GPIO.cleanup()
