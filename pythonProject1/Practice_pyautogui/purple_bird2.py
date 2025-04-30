import time

import pyautogui
import pygetwindow


window_titles = pygetwindow.getAllTitles()
for title in window_titles:
    print(title)


for i in range(60):
    target_window = pygetwindow.getWindowsWithTitle("linshif2@163.com")[0]
    target_window.activate()
    print(target_window.title)
    pyautogui.press("end")
    time.sleep(15)



