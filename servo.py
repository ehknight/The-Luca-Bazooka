import RPi.GPIO as GPIO
import time

class Servo:
    def __init__(self, pin_horizon, pin_vertical,xconst,yconst, x_res, y_res):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_horizon,GPIO.OUT)
        GPIO.setup(pin_vertical,GPIO.OUT)
        self.pwm_horizon = GPIO.PWM(pin_horizon, 50)
        self.pwm_vertical = GPIO.PWM(pin_vertical, 50)
        self.dc_horizon = 100
        self.dc_vertical = 100
        pwm_horizon.start(dc_horizon)
        pwm_vertical.start(dc_vertical)
        self.xconst = xconst  #dutycycle/pixel = (dutycyle per degree)/(pixel per degree)
        self.yconst = yconst
        self.x_res = x_res
        self.y_res = y_res

    def write_horizon(self,dc):
        self.pwm_horizon.ChangeDutyCycle(dc)

    def write_vertical(self, dc):
        self.pwm_vertical.ChangeDutyCycle(dc)

    def update_dx(self, dx):
        self.write_horizon(self.dc_horizon+dx*self.xconst)

    def update_dy(self, dy):
        self.write_vertical(self.dc_vertical+dy*self.yconst)

    def update (self, x, y):
        self.update_dx(x-(self.x_res/2))
        self.update_dy(y-(self.y_res/2))
