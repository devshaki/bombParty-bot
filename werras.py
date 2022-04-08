# import urllib.request
# from urllib.request import Request, urlopen
# fp = urllib.request.Request('https://jklm.fun/RZMF', headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(fp).read()
# a = str(webpage).split("\\n")
#
# for line in a:
#     print(line)
#     if '<div class="syllable">' in line:
#         print(line)
#         break
#
#
state = "auto"
used = []
import win32clipboard
from selenium import webdriver
from time import sleep
import requests
import keyboard
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import pyautogui
a = str(requests.get("http://norvig.com/ngrams/sowpods.txt").content).split("\\n")
# Create the webdriver object. Here the
# chromedriver is present in the driver
# folder of the root directory.
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
def work():
    pyautogui.doubleClick(810, 566)
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
    pyautogui.doubleClick(810, 566)
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

# get https://www.geeksforgeeks.org/
driver.get("https://jklm.fun")

# Maximize the window and let code stall
# for 10s to properly maximise the window.
driver.maximize_window()


while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('home'):  # if key 'q' is pressed
            work()
        if keyboard.is_pressed('end'):
            help()
        if keyboard.is_pressed('delete'):
            used.clear()

    except:
        pass



