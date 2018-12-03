import RoboPiLib as RPL
import setup
import time
x = 1
L = Pin
R = Pin

def lefttimefunk():
     global lefttime 
     lefttime = time.time()
def righttimefunk():
     global righttime 
     righttime = time.time()

def left():
     RPL.servoWrite(L,1410)

def lefts():
     RPL.servoWrite(L,1500)

def right():
     RPL.servoWrite(R,1590)

def right():
     RPL.servoWrite(R,1500)

lefttimefunk()
righttimefunk()
While x <= 60:
     time.sleep(0.05)
     rightpass = time.time() - righttime 
     leftpass = time.time() - leftitme
     if rightpass >= 2:
          righttimefunk()
     elif rightpass >= 1:
          rights()
     elif rightpass < 1:
          right()
     if leftpass >= 3:
	  lefttimefunk()
     elif leftpass >= 1.5:
          lefts()
     elif leftpass < 1.5:
          left()

