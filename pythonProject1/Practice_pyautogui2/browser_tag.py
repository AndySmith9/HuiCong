from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pygetwindow

# window_titles = pygetwindow.getAllTitles()
# for title in window_titles:
#     print(title)
# windows = pygetwindow.getWindowsWithTitle("Google Chrome")
# for window in windows:
#     print(window.title)

target_window = pygetwindow.getWindowsWithTitle("Google Chrome")[0]
target_window.activate()
# print(target_window.title)


options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
chrome_driver = webdriver.Chrome(options=options)
#chrome_driver.get("http://erpx.ksold.ltd:18085/store/product/walmart/template/add")
handles = chrome_driver.window_handles
for handle in handles:
    chrome_driver.switch_to.window(handle)
    # print(chrome_driver.title)
    if "添加模板 - 店铺管理系统" in chrome_driver.title:
        break

