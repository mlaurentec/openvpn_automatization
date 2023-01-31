from pyautogui import *
from time import sleep
import sys
import pyotp
totp = pyotp.TOTP("COLOCATUKEY")

def openvpn_autentication():
	x1, y1 = [21,745]

	moveTo(x1, y1)
	click()
	sleep(1)
	typewrite("OpenVPN", interval=0.2)
	sleep(1)
	x3, y3 = [189, 247] 
	moveTo(x3, y3) 
	click()
	sleep(1)
	moveTo(597, 217)
	click()
	sleep(1)
	code = totp.now()
	typewrite(code, interval=0.2)
	moveTo(671, 465)
	sleep(1)
	click()
	moveTo(908, 54)
	sleep(1)
	click()
	return 0


openvpn_autentication()