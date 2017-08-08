import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)  # Left motor input A
GPIO.setup(18, GPIO.OUT)  # Left motor input B
GPIO.setup(13, GPIO.OUT)  # Right motor input A
GPIO.setup(15, GPIO.OUT)  # Right motor input B
GPIO.setwarnings(False)

while True:
    print ("Rotating both motors in clockwise direction")
    GPIO.output(16, 1)
    GPIO.output(18, 0)
    GPIO.output(13, 1)
    GPIO.output(15, 0)
    time.sleep(1)  # One second delay

    print ("Rotating both motors in anticlockwise direction")
    GPIO.output(16, 0)
    GPIO.output(18, 1)
    GPIO.output(13, 0)
    GPIO.output(15, 1)
    time.sleep(1)
