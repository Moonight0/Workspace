import pyautogui
import time
import keyboard

time.sleep(3) 
 
while True:  
    
    pyautogui.click() 
    pyautogui.write("Oi, isso foi automático 😎")
    pyautogui.press("enter")

    if keyboard.is_pressed("esc"):
        break