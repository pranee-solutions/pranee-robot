import RPi.GPIO as GPIO  # Import GPIO library
import time

#from gpiozero import DistanceSensor
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

# ultrasonic = DistanceSensor(echo=17, trigger=4)
# initialize GPIO Pin as input
# GPIO.setup(led,GPIO.OUT)
GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RIGHT_MOTOR_1, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_2, GPIO.OUT)
GPIO.setup(LEFT_MOTOR_1, GPIO.OUT)
GPIO.setup(LEFT_MOTOR_2, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
# GPIO.output(led, 1)
time.sleep(5)


def calculateDistance():
    avgDistance = 0
    for i in range(5):
        GPIO.output(TRIG, False)  # Set TRIG as LOW
        time.sleep(0.1)  # Delay
        GPIO.output(TRIG, True)  # Set TRIG as HIGH
        time.sleep(0.00001)  # Delay of 0.00001 seconds
        GPIO.output(TRIG, False)  # Set TRIG as LOW
        pulse_start = time.time()
        pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start  # time to get back the pulse to sensor
        distance_l = pulse_duration * 17150  # Multiply pulse duration by 17150 (34300/2) to get distance
        distance_l = round(distance_l, 2)  # Round to two decimal points
        avgDistance = avgDistance + distance_l
    avgDistance = avgDistance / 5
    print "Distance coming as ", avgDistance
    #sensor = DistanceSensor(echo=ECHO, trigger=TRIG)
    #print "Distance: ", sensor.distance * 100
    return avgDistance


def stop():
    # print "stop"
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


def turnRightOfLeft():
    print "Stop called"
    stop()
    time.sleep(1)
    print "Back called"
    back()
    time.sleep(1.5)
    print "Right called"
    right()
    time.sleep(1.5)
    print "Stop called"
    stop()
    time.sleep(1)


flag = 0
try:
    while True:
        stop()
        j = GPIO.input(SWITCH)
        print "press switch to start Robo"
        if j == 1:  # Robot is activated when button is pressed
            flag = 1
            print "Robot Activated", j

        while flag == 1:
            distance = calculateDistance()
            if distance < 15:  # Obstacle detected
                print "Obstacle detected"
                turnRightOfLeft()
            else:
                time.sleep(0.5)
                forward()
            j = GPIO.input(SWITCH)
            if j == 1:  # De activate robot on pushin the button
                flag = 0
                print "Robot De-Activated", j
                stop()
                time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    stop()
    GPIO.cleanup()
