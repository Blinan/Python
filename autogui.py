# A programer control your cursor to draw a smile emoji
import pyautogui, time, math


def drawCircle(x, y, r, start_theta, end_theta, isClock):
    pyautogui.moveTo(x, y, duration=0.2)
    theta = start_theta
    
    
    if isClock == True:
        pyautogui.moveTo(x+r*math.cos(theta), y+r*math.sin(theta), duration=0.2)
        pyautogui.mouseDown()
        while theta > end_theta:
            pyautogui.moveTo(x+r*math.cos(theta), y+r*math.sin(theta), duration=0.01)
            theta -= 0.1
    else:
        pyautogui.moveTo(x-r*math.cos(theta), y-r*math.sin(theta), duration=0.2)
        pyautogui.mouseDown()
        while theta < end_theta:
            pyautogui.moveTo(x-r*math.cos(theta), y-r*math.sin(theta), duration=0.01)
            theta += 0.1
    pyautogui.mouseUp()



time.sleep(15)
pyautogui.click()
distance = 500
chance = 20
drawCircle(1500, 500, 250, 0, -2*math.pi, True)
drawCircle(1400, 440, 50, 0, math.pi, False)
drawCircle(1600, 440, 50, 0, math.pi, False)
drawCircle(1500, 575, 100, math.pi, 0, True)

pyautogui.moveTo(100, 100, duration=0.25)
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)
    distance = distance - chance
    pyautogui.drag(0, distance, duration=0.2)
    pyautogui.drag(-distance, 0, duration=0.2)
    distance = distance - chance
    pyautogui.drag(0, -distance, duration=0.2)
wh = pyautogui.size()



