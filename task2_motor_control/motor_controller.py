#try:
#from .fake_gpio import GPIO # For running app
#except ImportError:
import sys

from fake_gpio import GPIO # For running main
#import RPi.GPIO as GPIO # For testing in Raspberry Pi
from time import sleep
import random
# import ...

class MotorController(object):

  def __init__(self):
    self.working = [False]

  def start_motor(self):
    self.PIN_STEP = 25 # do not change
    self.PIN_DIR = 8 # do not change
    self.working = [True]
    CW = 1
    CCW = 0
    SPR90 = 400
    SPR270 = 1200
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.PIN_DIR, GPIO.OUT)
    GPIO.setup(self.PIN_STEP, GPIO.OUT)

    print('Motor started')
    delay = .0208

    motor_control = random.randint(1, 4)
    if motor_control == 1:
      GPIO.output(self.PIN_DIR, CW)
      for x in range (SPR90):
          GPIO.output(self.PIN_STEP, GPIO.HIGH)
          sleep(delay)
          GPIO.output(self.PIN_STEP, GPIO.LOW)
          sleep(delay)
      print("Rotating 90 degree in clockwise direction")
      self.working= ["Rotating 90 degree in clockwise direction"]
    if motor_control == 2:
      GPIO.output(self.PIN_DIR, CCW)
      for x in range (SPR90):
          GPIO.output(self.PIN_STEP, GPIO.HIGH)
          sleep(delay)
          GPIO.output(self.PIN_STEP, GPIO.LOW)
          sleep(delay)
      print("Rotating 90 degree in counter clockwise direction")
      self.working=["Rotating 90 degree in counter clockwise direction"]
    if motor_control == 3:
      GPIO.output(self.PIN_DIR, CW)
      for x in range (SPR270):
          GPIO.output(self.PIN_STEP, GPIO.HIGH)
          sleep(delay)
          GPIO.output(self.PIN_STEP, GPIO.LOW)
          sleep(delay)
      print("Rotating 270 degree in clockwise direction")
      self.working=["Rotating 270 degree in clockwise direction"]
    if motor_control == 4:
      GPIO.output(self.PIN_DIR, CCW)
      for x in range (SPR270):
          GPIO.output(self.PIN_STEP, GPIO.HIGH)
          sleep(delay)
          GPIO.output(self.PIN_STEP, GPIO.LOW)
          sleep(delay)
      print("Rotating 270 degree in counter clockwise direction")
      self.working=["Rotating 270 degree in counter clockwise direction"]

    GPIO.cleanup()
    print("Clean program exit.")
    #self.working = [False]

  def is_working(self):
    return self.working
