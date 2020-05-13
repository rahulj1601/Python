import pyautogui

pyautogui.click()

distance = 500
while distance > 0:
    pyautogui.dragRel(distance,0, duration=1, button='left')
    distance -= 10
    
    pyautogui.dragRel(0, distance, duration=1, button='left')
    
    pyautogui.dragRel(-distance, 0, duration=1, button='left')
    distance -= 10

    pyautogui.dragRel(0, -distance, duration=1, button='left')    
