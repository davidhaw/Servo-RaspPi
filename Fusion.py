import sys, getopt

sys.path.append('.')

import pigpio
import RTIMU
import os.path
import time
import math


pi = pigpio.pi()
pi.set_mode(18, pigpio.OUTPUT)
pi.set_mode(23, pigpio.OUTPUT)
b = 1250
a = 1250

pi.set_servo_pulsewidth(18, a)
pi.set_servo_pulsewidth(23, b)
SETTINGS_FILE = "RTIMULib"

print("Using settings file " + SETTINGS_FILE + ".ini")
if not os.path.exists(SETTINGS_FILE + ".ini"):
  print("Settings file does not exist, will be created")

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

print("IMU Name: " + imu.IMUName())

if (not imu.IMUInit()):
    print("IMU Init Failed")
    sys.exit(1)
else:
    print("IMU Init Succeeded")

# this is a good time to set any fusion parameters

imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)

poll_interval = imu.IMUGetPollInterval()
print("Recommended Poll Interval: %dmS\n" % poll_interval)

#data = imu.getIMUData()
#fusionPose = data["fusionPose"]
#print(math.degrees(fusionPose[0]))
#print(math.degrees(fusionPose[0]))
z = 1500
pi.set_servo_pulsewidth(18, z)
while True:

  if imu.IMURead():
    # x, y, z = imu.getFusionData()
# print("%f %f %f" % (x,y,z))
    data = imu.getIMUData()
    fusionPose = data["fusionPose"]
#    print("r: %f p: %f y: %f" % (math.degrees(fusionPose[0]), 
#        math.degrees(fusionPose[1]), math.degrees(fusionPose[2])))
    print(math.degrees(fusionPose[0]))
    g = math.degrees(fusionPose[0])
    if g > 10:
      z+=15
      pi.set_servo_pulsewidth(18, z)
      print(z)
      g = math.degrees(fusionPose[0])
      time.sleep(0.10)

    if g < -10:
      z-=15
      pi.set_servo_pulsewidth(18, z)
      print(z)
      g = math.degrees(fusionPose[0])
      time.sleep(0.10)
    if g > 10:
      print("POOOOOOOOOO")
      z+=15
      pi.set_servo_pulsewidth(18,z)
      time.sleep(0.10)
# a = math.degrees(fusionPose[0])

      #pi.set_servo_pulsewidth(18, c)
      #print(c)

