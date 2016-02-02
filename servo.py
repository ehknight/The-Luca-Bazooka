import RPi.GPIO as GPIO
import time

class Servo:
    def __init__(self, pin_horizon, pin_vertical,xconst,yconst):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_horizon,GPIO.OUT)
        GPIO.setup(pin_vertical,GPIO.OUT)
        self.pwm_horizon = GPIO.PWM(pin_horizon, 50)
        self.pwm_vertical = GPIO.PWM(pin_vertical, 50)
        self.dc_horizon = 100
        self.dc_vertical = 100
        pwm_horizon.start(dc_horizon)
        pwm_vertical.start(dc_vertical)
        self.xconst = xconst
        self.yconst = yconst

    def write_horizon(self,dc):
        self.pwm_horizon.ChangeDutyCycle(dc)

    def write_vertical(self, dc):
        self.pwm_vertical.ChangeDutyCycle(dc)

    def update_dx(self, dx):
        self.write_horizon(self.dc_horizon+dx*self.xconst)

    def update_dy(self, dy):
        self.write_vertical(self.dc_vertical+dy*self.yconst)


