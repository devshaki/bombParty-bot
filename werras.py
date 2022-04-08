import ctypes
import win32clipboard
from selenium import webdriver
from time import sleep
import requests
import keyboard
import webdriver_manager
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import pyautogui
used = []
a = str(requests.get("http://norvig.com/ngrams/sowpods.txt").content).split("\\n")
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
width, height = screensize
Wyahas = 1920/width
Hyahas = 1080/height
print(Wyahas)
textpos1 = 810 * Wyahas
textpos2 = 566 * Hyahas
writepos1 = 800 * Wyahas
writepos2 = 1013 * Hyahas
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
def work():
    pyautogui.doubleClick(textpos1,textpos2)
    pyautogui.keyDown("ctrl")
    pyautogui.press("c")
    pyautogui.keyUp("ctrl")
    win32clipboard.OpenClipboard()
    data = str(win32clipboard.GetClipboardData()).upper()
    win32clipboard.CloseClipboard()
    pyautogui.click(writepos1,writepos2)
    for i in range(len(a)):
        if data in a[i]:
            if any(a[i] in s for s in used):
                pass
            else:
                pyautogui.typewrite(a[i])
                pyautogui.press("Enter")
                used.append(a[i])
                break

def help():
    pyautogui.doubleClick(textpos1,textpos2)
    pyautogui.keyDown("ctrl")
    pyautogui.press("c")
    pyautogui.keyUp("ctrl")
    win32clipboard.OpenClipboard()
    data = str(win32clipboard.GetClipboardData()).upper()
    win32clipboard.CloseClipboard()
    pyautogui.click(1789,1024)
    for i in range(len(a)):
        if data in a[i]:
            if any(a[i] in s for s in used):
                pass
            else:
                pyautogui.typewrite(a[i])
                pyautogui.press("Enter")
                used.append(a[i])
                break



driver.get("https://jklm.fun")

driver.maximize_window()


while True:
    try:
        if keyboard.is_pressed('home'):
            work()
        if keyboard.is_pressed('end'):
            help()
        if keyboard.is_pressed('delete'):
            used.clear()


    except:
        pass



