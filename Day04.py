import pyautogui
if (pyautogui.prompt('Do you want to begin auto scroll? Enter 0 or 1: '))=='1':
  pyautogui.alert('!!To stop move mouse to top left!!')
  pyautogui.middleClick()
  pyautogui.moveRel(0,25)
  

#------------------------
import time
pyautogui.alert('Remember!!!Move your mouse to top left to stop!!!')
x,y=pyautogui.size()
pyautogui.moveTo(x/4,3*y/4)
pyautogui.click()
pyautogui.dragRel(0,-300)
pyautogui.dragRel(400,0)
pyautogui.dragRel(-50,-100)
pyautogui.dragRel(-300,0)
pyautogui.dragRel(-50,100)
pyautogui.dragRel(50,-100)
pyautogui.dragRel(50,100)
pyautogui.dragRel(0,300)
pyautogui.dragRel(-100,0)
pyautogui.dragRel(400,0)
pyautogui.dragRel(0,-300)
