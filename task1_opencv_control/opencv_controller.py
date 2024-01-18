#try:
#from .camera import Camera # For running app
#except ImportError:
from camera import Camera # For running main

#from pi_camera import Camera # For Raspberry Pi

#class OpenCVController(object):

 #   def __init__(self):
  #      self.current_color = [False,False,False]
   #     self.camera = Camera()
    #    print('OpenCV controller initiated')

 #   def process_frame(self):
 #       frame = self.camera.get_frame()
 #       # ....
  #      print('Monitoring')
   #     return frame

 #   def get_current_color(self):
  #      return self.current_color

import cv2
import numpy as np

class OpenCVController(object):

    def __init__(self):
        self.current_color = [False, False, False]
        print('OpenCV controller initiated')

    def process_frame(self, camera):
        frame = Camera.process_frame()
        # lower and upper values for red
        red_lower = np.array([0, 70, 50], np.uint8)
        red_upper = np.array([10, 255, 255], np.uint8)
        # Function call to detect red and mark it
        image, red_rect = self.color_label(
            frame, red_upper, red_lower, "mark", (0, 0, 255))
        # lower and upper values for green
        green_lower = np.array([25, 40, 100], np.uint8)
        green_upper = np.array([70, 255, 255], np.uint8)
        # Function call to detech green and label it green
        image, green_rect = self.color_label(
            image, green_upper, green_lower, "green", (0, 255, 0))
            # lower and upper value values for yellow
        yellow_lower = np.array([22, 130, 105], np.uint8)
        yellow_upper = np.array([48, 255, 200], np.uint8)
        # Function call to detect yellow and label it
        image, yellow_rect = self.color_label(
            image, yellow_upper, yellow_lower, "yellow", (0, 255, 255))
             # lower and upper value of purple
        purple_lower = np.array([130, 0, 20], np.uint8)
        purple_upper = np.array([150, 100, 255], np.uint8)
        # Function call to detect purple and label it
        image, purple_rect = self.color_label(
            image, purple_upper, purple_lower, "purple", (255, 0, 255))
        
        self.current_color = self.doOverlap(red_rect, green_rect,purple_rect,yellow_rect)
       
        print('Monitoring')
        return image

    def color_label(self, frame, upper, lower, text, color):
        res = (0, 0, 0, 0)
        imageFrame = np.fromstring(frame, np.uint8)
        # BGR to HSV for image processiing
        imageFrame = cv2.imdecode(imageFrame, cv2.COLOR_BGR2RGB)
        hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
        # red color masking range
        red_mask = cv2.inRange(hsvFrame, lower, upper)
        #  We can filter and modify images by interacting with their pixels; Kernels represent the area for each operation
        kernal = np.ones((20, 20), "uint8")
        # dilation used for removing noise
        red_mask = cv2.dilate(red_mask, kernal)
        # bitwise condition to take red region only
        res_red = cv2.bitwise_and(imageFrame, imageFrame, mask=red_mask)
        # tracking red color using contours
        contours, hierarchy = cv2.findContours(
            red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        max_Area = 0
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > 300):
                # ractange creation
                global x, y, w, h
                x, y, w, h = cv2.boundingRect(contour)
            if(area > max_Area):
                max_Area = area
                res = (x, y, w, h)
        x, y, w, h = res
        imageFrame = cv2.rectangle(
            imageFrame, (x, y), (x + w, y + h), color, 2)
        # Label creation
        cv2.putText(imageFrame, text, (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, color)
        #  convert the image format into streaming data and assign it to memory cache
        img_str = cv2.imencode('.jpg', imageFrame)[1].tostring()
        return img_str, res


    def get_current_color(self):
        return self.current_color
    
    def doOverlap(self, red1, green2, purple3, yellow4):

        # Intersection area
        x1, y1, w1, h1 = red1
        x2, y2, w2, h2 = green2
        x3, y3, w3, h3 = purple3
        x4, y4, w4, h4 = yellow4
        # conditions for "current color from opencv"
        if (x1+w1 <= x2+w2) and (w2+h2 >= w1+h1):
            return [True, False, False]
        elif (x1 <= x3):
            return [True, True, False]
        elif (x1+w1 <= x3+w3) and (w3+h3 >= w1+h1):
            return [False, True, False]
        elif (x1 <= x4):
            return [False, True, True]        
        elif (x1+w1 <= x4+w4) and (w4+h4 >= w1+h1):
            return [False, False, True]
