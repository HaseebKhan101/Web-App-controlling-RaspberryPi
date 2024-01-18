#try:
 #   from .fake_gpio import GPIO # For running app
#except ImportError:
import statistics

from fake_gpio import GPIO # For running main
# import RPi.GPIO as GPIO # For testing in Raspberry Pi
import time
from statistics import median

class SensorController:

  def __init__(self):
    self.PIN_TRIGGER = 18 # do not change
    self.PIN_ECHO = 24 # do not change
    self.distance = None
    self.color_from_distance = [False, False, False]
    print('Sensor controller initiated')
    #by Group F
    #GPIO.setmode(GPIO.BCM)

  def track_rod(self):
    # ...
    #global pulse_end, pulse_start
    pulse_end=0
    pulse_start=0
    counter=0
    Max20=5
    median=[]
    while counter < Max20:
        #by Group F
        GPIO.setmode(GPIO.BCM)
        print("distance measurement in progress")
        GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(self.PIN_ECHO, GPIO.IN)
        GPIO.setup(self.PIN_TRIGGER, False)
        print("waiting for sensor to settle")
        time.sleep(0.2)
        GPIO.output(self.PIN_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(self.PIN_TRIGGER, False)
        while GPIO.input(self.PIN_ECHO)==0:
            pulse_start=time.time()
        while GPIO.input(self.PIN_ECHO)== 1:
            pulse_end=time.time()
        pulse_duration = pulse_end - pulse_start
        distance=pulse_duration*17150
        self.distance=round(distance*2)
        print("distance:", self.distance, " cm")
        time.sleep(2)
        print('Monitoring')
        GPIO.cleanup()
        median.append(self.distance)
        counter=counter+1
    print("average", median)
    print("average2", statistics.median(median))
  def get_distance(self):
    return self.distance

  def get_color_from_distance(self):
    return self.color_from_distance