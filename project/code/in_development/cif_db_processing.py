import time
import pyautogui

print(pyautogui.size())


# print(pyautogui.position())
# pyautogui.moveTo(830, 785, duration = 1)

def file_open():
    pyautogui.click(20, 390)
    pyautogui.click(35, 415)


def juan_folder():
    pyautogui.click(700, 690)
    pyautogui.click(700, 690)


def load_file():
    pyautogui.click(1000, 630)
    pyautogui.click(900, 840)
    pyautogui.click(830, 785)
    pyautogui.click(830, 785)


def calculate():
    pyautogui.click(250, 390)
    pyautogui.click(310, 555)


file_open()
time.sleep(1)
juan_folder()
time.sleep(1)
load_file()
time.sleep(1)
calculate()
time.sleep(1)

pyautogui.click(890, 695)
pyautogui.click(890, 695)

pyautogui.click(1230, 1035)

juan_folder()

while True:
    print(pyautogui.position())
    time.sleep(2)
