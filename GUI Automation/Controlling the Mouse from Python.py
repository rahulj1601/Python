import pyautogui

width, height = pyautogui.size() #screen resolution is returned

print(width)
print(height)
print(pyautogui.position()) #position of mouse when the program is run

pyautogui.moveTo(10,10) #moves the mouse to these coordinates

pyautogui.moveTo(300,500, duration=5) #moves in specific amount of seconds

pyautogui.moveRel(200, 0, duration=2) #move relative to current position
pyautogui.moveRel(0, -100, duration=2) #move up

pyautogui.click(451,11)
#pyautogui.doubleClick()
#pyautogui.rightClick()
#pyautogui.middleClick()

#pyautogui.dragRel()
#pyautogui.dragTo()

#Fail Safe - Drag mouse into (0,0)
