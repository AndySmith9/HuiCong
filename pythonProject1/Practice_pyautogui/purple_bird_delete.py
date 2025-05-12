import time

import pyautogui
import pygetwindow





circle_times = None
window = None
sleep = None
textfield_x = None
textfield_y = None
checkbox_x = None
checkbox_y = None
combobox1_x = None
combobox1_y = None
combobox2_x = None
combobox2_y = None
button1_x = None
button1_y = None

window_titles = pygetwindow.getAllTitles()
for title in window_titles:
    print(title)

file = open("purple_bird_delete.txt","r",encoding="UTF-8")
lines = file.readlines()
for line in lines:
    if "#" not in line:
        circle_times = int(line.split(",")[0])
        print("circle_times:"+str(circle_times))
        window = line.split(",")[1]
        sleep = int(line.split(",")[2])
        print("sleep:"+str(sleep))
        textfield_x = int(line.split(",")[3])
        print("textfield_x:"+str(textfield_x))
        textfield_y = int(line.split(",")[4])
        print("textfield_y:"+str(textfield_y))
        checkbox_x = int(line.split(",")[5])
        checkbox_y = int(line.split(",")[6])
        combobox1_x = int(line.split(",")[7])
        combobox1_y = int(line.split(",")[8])
        combobox2_x = int(line.split(",")[9])
        combobox2_y = int(line.split(",")[10])
        button1_x = int(line.split(",")[11])
        button1_y = int(line.split(",")[12])


for i in range(circle_times):
    target_window = pygetwindow.getWindowsWithTitle(window)[0]
    target_window.activate()
    print(target_window.title)
    pyautogui.leftClick(textfield_x,textfield_y)
    # time.sleep(1)
    x,y = pyautogui.position()
    print(f"坐标:{x},{y}")
    pyautogui.hotkey("ctrl","a")
    # time.sleep(1)
    pyautogui.press("delete")
    pyautogui.typewrite("KO5484640816")
    # time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(checkbox_x,checkbox_y)
    pyautogui.click(combobox1_x,combobox1_y)
    pyautogui.click(combobox2_x,combobox2_y)
    pyautogui.click(button1_x,button1_y)
    time.sleep(13)
    pyautogui.press("f5")


file.close()
