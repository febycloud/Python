#!/usr/bin/python
import time
import pyautogui
import webbrowser
url='https://tinder.com/'
webbrowser.open(url)
time.sleep(10)
i=0
for i in range(0,100):
	i+=1
	pyautogui.press('right')
	time.sleep(0.5)