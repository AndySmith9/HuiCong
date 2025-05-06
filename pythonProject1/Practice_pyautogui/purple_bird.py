import time

import pyautogui
import pygetwindow


window_titles = pygetwindow.getAllTitles()
for title in window_titles:
    print(title)

file = open("purple_bird.txt","r",encoding="UTF-8")
lines = file.readlines()
for line in lines:
    if "#" not in line:
        circle_times = int(line.split(",")[0])
        print("circle_times:"+str(circle_times))
        window = line.split(",")[1]
        sleep = int(line.split(",")[2])
        print("sleep:"+str(sleep))


for i in range(circle_times):
    target_window = pygetwindow.getWindowsWithTitle(window)[0]
    target_window.activate()
    print(target_window.title)
    pyautogui.press("end")
    time.sleep(sleep)


file.close()
