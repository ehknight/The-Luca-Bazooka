import RPi.GPIO as GPIO
import servo

class Memes:
    def __init__(self):
        servo = servo.Servo(8,10,53.5/640,41.41/480,640,480)
        memeconstant = 1 #Change constant to taste
    def goToPixel(self, x, y):
        centerX = 640/2
        centerY = 480/2
        xMove = 1
        yMove = 1
        if x < centerX:
            xMove = -1
        if y < centerY:
            yMove = -1
        for meme in range(0, 
