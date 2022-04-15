from PIL import ImageGrab
import time
import pyautogui

#Dino Chrome Game Bot 

# Region of detections
# Coordenates for resolution 1366x768
X = 450.5
X2 = 565.2
# Detects enemy by diff in pixel color in region of detections
def detect_enemy(screem):
    for x in range(int(X), int(X2)):
        for y in range(303, 335):
            cor = screem.getpixel((x, y))
            if cor == (83, 83, 83):
                return True  #Return True for a detected enemy
def jump():
    global X
    global X2
    pyautogui.press('Up')
    X += 0.5
    X2 += 0.4 ## Increment in detection region for increase speed of game



# Take screenshot using PIL lib
def grab():
    return ImageGrab.grab()


time.sleep(4)
print('iniciado')
# Infinite Loop of bot
while True:
    enemy = grab()
    if detect_enemy(enemy):
        jump()



