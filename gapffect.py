import random
import time
import pyautogui as pag

rewards = ["","","",""]

for _ in range(45):
    time.sleep(random.randrange(90,130))
    pag.alert(text="Take a break", title="gap affect")
    time.sleep(10)
    pag.alert(text="Continue", title="gap affect")


pag.alert(text="STOP WORKING", title="gap affect")
