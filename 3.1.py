import RoboPiLib as RPL
import setup
import time
x = 1
while x == 1:
     RPL.servoWrite(0, 1590)
     time.sleep(1)
     RPL.servoWrite(0, 1500)
     time.sleep(1)

