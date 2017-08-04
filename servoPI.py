import RPi.GPIO as GPIO
import time
import pigpio

pi = pigpio.pi()
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(1, GPIO.IN)
GPIO.setup(14, GPIO.IN)
pi.set_mode(18, pigpio.OUTPUT)
pi.set_mode(23, pigpio.OUTPUT)
b = 1250
a = 1250

pi.set_servo_pulsewidth(18, a)
pi.set_servo_pulsewidth(23, b)

while True:
        input = GPIO.input(24)
        input2 = GPIO.input(16)
        input3 = GPIO.input(1)
        input4 = GPIO.input(14)
        if (GPIO.input(24)):
                if (a < 2500):
                        a = a + 10
                        pi.set_servo_pulsewidth(18, a)
                        print(a)
        if(GPIO.input(16)):
                a = a - 10
                pi.set_servo_pulsewidth(18, a)
                print(a)
        if(GPIO.input(1)):
                b = b + 10
                pi.set_servo_pulsewidth(23, b)
                print(b)
        if(GPIO.input(14)):
                b = b - 10
                pi.set_servo_pulsewidth(23, b)
                print(b)

        time.sleep(0.25)


