import RPi.GPIO as GPIO  # Import GPIO library
import time
from gpiozero import DistanceSensor
# Import time library
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
TRIG = 4
ECHO = 17
SWITCH = 18
# led = 22
RIGHT_MOTOR_1 = 27
RIGHT_MOTOR_2 = 22
LEFT_MOTOR_1 = 24
LEFT_MOTOR_2 = 23

ultrasonic = DistanceSensor(echo=17, trigger=4)
# initialize GPIO Pin as input
# GPIO.setup(led,GPIO.OUT)
GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RIGHT_MOTOR_1, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_2, GPIO.OUT)
GPIO.setup(LEFT_MOTOR_1, GPIO.OUT)
GPIO.setup(LEFT_MOTOR_2, GPIO.OUT)
# GPIO.output(led, 1)
time.sleep(5)


def stop():
    #print "stop"
    GPIO.output(RIGHT_MOTOR_1, 0)
    GPIO.output(RIGHT_MOTOR_2, 0)
    GPIO.output(LEFT_MOTOR_1, 0)
    GPIO.output(LEFT_MOTOR_2, 0)


def forward():
    GPIO.output(RIGHT_MOTOR_1, 1)
    GPIO.output(RIGHT_MOTOR_2, 0)
    GPIO.output(LEFT_MOTOR_1, 1)
    GPIO.output(LEFT_MOTOR_2, 0)
    print "Forward"


def back():
    GPIO.output(RIGHT_MOTOR_1, 0)
    GPIO.output(RIGHT_MOTOR_2, 1)
    GPIO.output(LEFT_MOTOR_1, 0)
    GPIO.output(LEFT_MOTOR_2, 1)
    print "back"


def left():
    GPIO.output(RIGHT_MOTOR_1, 0)
    GPIO.output(RIGHT_MOTOR_2, 0)
    GPIO.output(LEFT_MOTOR_1, 1)
    GPIO.output(LEFT_MOTOR_2, 0)
    print "left"


def right():
    GPIO.output(RIGHT_MOTOR_1, 1)
    GPIO.output(RIGHT_MOTOR_2, 0)
    GPIO.output(LEFT_MOTOR_1, 0)
    GPIO.output(LEFT_MOTOR_2, 0)
    print "right"

flag = 0
count = 0
while True:
    stop()
    j = GPIO.input(SWITCH)
    print "press switch to start Robo"
    if j == 1:  # Robot is activated when button is pressed
        flag = 1
        print "Robot Activated"
        time.sleep(2)
    while flag == 1:
        distance = ultrasonic.distance * 100
        distance = round(distance, 2)  # Round to two decimal points
        count = 0
        print "Distance coming as ", distance
        if distance < 15:  # Check whether the distance is within 15 cm range
            count = count + 1
            print "Stop called"
            stop()
            time.sleep(1)
            print "Back called"
            back()
            time.sleep(1.5)
            if (count % 3 == 1) & (flag == 0):
                print "Right called"
                right()
            else:
                print "Left called"
                left()
            time.sleep(1.5)
            print "Stop called"
            stop()
            time.sleep(1)
        else:
            print "Forward called"
            forward()
            j = GPIO.input(SWITCH)
            if j == 1:  # De activate robot on pushin the button
                print "Robot De-Activated", j
                stop()
                time.sleep(1)
                flag = 0

