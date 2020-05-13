import pyautogui
pyautogui.click(100,100); pyautogui.typewrite('Hello world!', interval=0.2)
#split commands with a semicolon to perform them immediately after one another
#interval gives a pause between each character

pyautogui.click(100,100); pyautogui.typewrite(['a','b','left','left','X','Y'], interval=1)
# left key shifts the mouse a character to the left
print(pyautogui.KEYBOARD_KEYS) #displays all the possible keys which can be accessed

pyautogui.press('f1') #activate a specific key

pyautogui.hotkey('command', 'n') #press a series of keys at the same time
