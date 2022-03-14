import pywinauto
import time
import pynput
import win32api
import pyautogui as pag

win32api.ShellExecute(0,'open','C:/Program Files/ArcGIS/Pro/bin/ArcGISPro.exe','C:/Users/User/Desktop/GIS/自動化/自動化.aprx','',0)


time.sleep(30)

ctr = pynput.keyboard.Controller()

pag.click(1000,600,button='left')

time.sleep(3)

with ctr.pressed(
    pynput.keyboard.KeyCode.from_vk(17),
    pynput.keyboard.KeyCode.from_vk(16),
    'r'):pass

print('成功拉')


"""
app = pywinauto.application.Application()

app.start("C:/Program Files/ArcGIS/Pro/bin/ArcGISPro.exe")


time.sleep(5)

print("開啟GIS成功")

ctr = pynput.keyboard.Controller()

with ctr.pressed(
    pynput.keyboard.KeyCode.from_vk(17),
    'o'):pass

time.sleep(5)

"""