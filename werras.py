
used = []
import win32clipboard
from selenium import webdriver
from time import sleep
import requests
import keyboard
import webdriver_manager
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import pyautogui
a = str(requests.get("http://norvig.com/ngrams/sowpods.txt").content).split("\\n")

pos = 810, 566
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
def work():
    pyautogui.doubleClick(pos)
    pyautogui.keyDown("ctrl")
    pyautogui.press("c")
    pyautogui.keyUp("ctrl")
    win32clipboard.OpenClipboard()
    data = str(win32clipboard.GetClipboardData()).upper()
    win32clipboard.CloseClipboard()
    pyautogui.click(800,1013)
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
    pyautogui.doubleClick(pos)
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
def getPos():
    pos = pyautogui.position()


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
        if keyboard.is_pressed('f4'):
            getPos()

    except:
        pass



