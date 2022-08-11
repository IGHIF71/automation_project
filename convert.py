
import json
import time
import re
import pyautogui
import os
import glob

path = "C:\\Users\\Khalil\Music\\test\\*.mp3"

class convert:
    def __init__(self) -> None:
       self.files = []
       for file in glob.iglob(path, recursive=True):
        self.files.append(file)
       
    def get_size():
        print(pyautogui.size())
    def get_length(self):
        return len(self.files)
    def get_pos():
        print(pyautogui.position())
    def start_audacity():
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Audacity.lnk")
    def stop_audacity():
        os.close("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Audacity.lnk")
    def locate_ui_element(image):
        location = pyautogui.locateOnScreen(image, grayscale = True, confidence = 0.8)
        return(pyautogui.center(location))
    def move_mouse(cor):
        pyautogui.moveTo(cor)
    def click():
        pyautogui.click()
    def select_effect(self):
        pyautogui.hotkey("ctrl", "a")
        effect_button_location = convert.locate_ui_element("effect.png")
        convert.move_mouse(effect_button_location)
        convert.click()
    def prepare_application(self):
        convert.start_audacity()
    def select_file(self):
        button_location = convert.locate_ui_element("file.png")
        convert.move_mouse(button_location)
        convert.click()
    def select_open(self):
        button_location = convert.locate_ui_element("open.png")
        convert.move_mouse(button_location)
        convert.click()
    def get_file(self, number):
        return self.files[number]
    def open_file(self):
        button_location = convert.locate_ui_element("open_file.png")
        convert.move_mouse(button_location)
        convert.click()
    def change_pitch(self):
        button_location = convert.locate_ui_element("change_pitch.png")
        convert.move_mouse(button_location)
        convert.click()
        time.sleep(2)
        pyautogui.press('tab', presses=5)
        pyautogui.write('440')
        pyautogui.press('tab')
        pyautogui.write('432')
    def select_ok(self):
        button_location = convert.locate_ui_element("ok.png")
        convert.move_mouse(button_location)
        convert.click()
    def export_file(self):
        button_location = convert.locate_ui_element("export.png")
        convert.move_mouse(button_location)
        convert.click()
        time.sleep(1)
        button_location = convert.locate_ui_element("export_as_mp3.png")
        convert.move_mouse(button_location)
        convert.click()
    def save_files(self):
        button_location = convert.locate_ui_element("save.png")
        convert.move_mouse(button_location)
        convert.click()
    def close_application(self):
        button_location = convert.locate_ui_element("exit.png")
        convert.move_mouse(button_location)
        convert.click()
        time.sleep(1)
        button_location = convert.locate_ui_element("no.png")
        convert.move_mouse(button_location)
        convert.click()
    def convert_to_432(self, file_number):
        self.prepare_application()
        time.sleep(3)
        self.select_file()
        time.sleep(3)
        self.select_open()
        time.sleep(1)
        pyautogui.write(self.get_file(file_number))
        time.sleep(1)
        self.open_file()
        time.sleep(2)
        self.select_effect()
        time.sleep(2)
        self.change_pitch()
        time.sleep(1)
        self.select_ok()
        time.sleep(200)
        self.select_file()
        time.sleep(1)
        self.export_file()
        time.sleep(3)
        self.save_files()
        time.sleep(10)
        self.close_application()


    
convert1 = convert()
num_files = convert1.get_length()
for files in range(num_files):
    time.sleep(2)
    convert1.convert_to_432(files)





