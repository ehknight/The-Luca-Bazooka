import RPi.GPIO as GPIO
import time

class Servo: #Main servo class
    def __init__(self, pin_horizon, pin_vertical,xconst=0,yconst=0, x_res=0, y_res=0, xinit = 0, yinit =0):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_horizon,GPIO.OUT)
        GPIO.setup(pin_vertical,GPIO.OUT)
        self.pwm_horizon = GPIO.PWM(pin_horizon, 100)
        self.pwm_vertical = GPIO.PWM(pin_vertical, 100)
        self.angle_horizon = xinit  #angles such that laser dot is centered in camera
        self.angle_vertical = yinit
        self.yinit = yinit  
        self.pwm_horizon.start(xinit/10.0+2.5)
        self.pwm_vertical.start(yinit/10.0+2.5)
        #self.write_horizon(xinit)
        #self.write_vertical(yinit)
        self.xconst = xconst  #angle/pixel
        self.yconst = yconst
        self.x_res = x_res
        self.y_res = y_res
        time.sleep(1)
        print("GPIO set up ready")

    def write_horizon(self,angle): #Change horizontal servo
        dc = float(angle)/10.0+2.5
        self.pwm_horizon.ChangeDutyCycle(dc)
        print ("dc horizon is: %s" %dc)
        time.sleep(0.01)
    def write_vertical(self, angle): #For vertical servo
        dc = float(angle)/10.0+2.5
        self.pwm_vertical.ChangeDutyCycle(dc)
        print ("dc vertical is:%s"%dc)
        time.sleep(0.01)
    def update_dx(self, dx):  #update the x axis 
        temp = self.angle_horizon + dx
        if temp>=180:
            self.angle_horizon = 180
        elif temp<=0:
            self.angle_horizon = 0
        else:
            self.angle_horizon = temp
        self.write_horizon(self.angle_horizon)

    def update_dy(self, dy): #updateing the y axis from deflection angle
        self.angle_vertical = self.yinit-dy
        self.write_vertical(self.angle_vertical)

    def update (self, x, y):   #input the pixel x, y where object is found
        self.update_dx(self.xconst*(x-(self.x_res/2)))
        self.update_dy(self.yconst*(y-(self.y_res/2)))
