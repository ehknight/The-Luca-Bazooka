import RPi.GPIO as GPIO
import time

class Servo:
    def __init__(self, pin_horizon, pin_vertical,xconst=0,yconst=0, x_res=0, y_res=0):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_horizon,GPIO.OUT)
        GPIO.setup(pin_vertical,GPIO.OUT)
        self.pwm_horizon = GPIO.PWM(pin_horizon, 100)
        self.pwm_vertical = GPIO.PWM(pin_vertical, 100)
        self.angle_horizon = 0
        self.angle_vertical = 0
        self.pwm_horizon.start(0)
        self.pwm_vertical.start(0)
        self.xconst = xconst  #angle/pixel
        self.yconst = yconst
        self.x_res = x_res
        self.y_res = y_res

    def write_horizon(self,angle):
        dc = float(angle)/10.0+2.5
        self.pwm_horizon.ChangeDutyCycle(dc)
        time.sleep(0.1)
    def write_vertical(self, angle):
        dc = float(angle)/10.0+2.5
        self.pwm_vertical.ChangeDutyCycle(dc)
        time.sleep(0.1)
    def update_dx(self, dx):
        self.angle_horizon += dx
        self.write_horizon(self.angle_horizon)

    def update_dy(self, dy):
        self.angle_vertical += dy
        self.write_vertical(self.angle_vertical)

    def update (self, x, y):   #input the pixel x, y where object is found
        self.update_dx(self.xconst*(x-(self.x_res/2)))
        self.update_dy(self.yconst*(y-(self.y_res/2)))
