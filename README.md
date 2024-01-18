# Web App controlling the Raspberry Pi

The project was done as a preparatory course in my Master of Media Technology in Technical University, Ilmenau, Germany.

## Milestones of Project Achieved:

• Understanding the hardware capabilities of Raspberry PI
• Using SSH in configuring and managing the Raspberry Pi remotely
•Used Python to complete the project, while working with libraries like opencv, numpy, RPi.GPIO, flask, gunicorn, picamera and others
• HTML, CSS, Javascipt used for creating the frontend of the app

## Three subtasks were achieved during the project

• Using opencv library to detect different color ranges using picamera
• Using step motor to control the rod moving using raspberry pi GPIO
• Using sensor controller (ultrasonic sensor to measure the distance using raspberry pi)

# Project content

This repository contains the base folders to conduct each task, as follows:

## Sub-Tasks

Each folder have the script for its respective code to run on raspberry pi. Each folder has a `main.py` script to test the code. The folders are:

| Task |               Folder |
| ---: | -------------------: |
|    1 | task1_opencv_control |
|    2 |  task2_motor_control |
|    3 | task3_sensor_control |

The results of previous tasks is going to be employed by a Flask web application. Take the following information into account:

1. _requirements.txt_: this file contains the libraries that you might required for running the app. After creating your environment you should install these libraries as follows:

```
pip install -r requirements.txt
```

Use _requirements_raspi.txt_ for Raspberry Pi.

2. _app.py_: this file is a script to run the Flask application. This application should work even if you haven't completed previous tasks. I will just do dummy things, like printing messages on the development server console.
3. _static_: this folder contains the main client-side script of this application.
4. _templates_: this folder contains the index template since this is a one-page application.
