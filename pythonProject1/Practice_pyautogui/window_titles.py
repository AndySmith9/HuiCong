
import pygetwindow


file = open("windowsTitles.txt","w",encoding="UTF-8")

window_titles = pygetwindow.getAllTitles()
for title in window_titles:
    print(title)
    file.write(title+"\n")

file.close()




