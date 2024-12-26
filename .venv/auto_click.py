import tkinter as tk
from colorsys import rgb_to_hls

import pynput
import time
import keyboard
from pynput.mouse import Controller,Button


multiPos = False
loopedClick = False
click = False
clickNumb = 0
interval = 0.05
cords = []
mouse = Controller()
root = tk.Tk()
root.title("AutoClicker")

root.geometry("300x350")

label1 = tk.Label(root, text="number of clicks:")
label1.pack(pady=5)

entry1 = tk.Entry(root, width=10)
entry1.pack(pady=5)

label2 = tk.Label(root, text="interval:")
label2.pack(pady=5)

entry2 = tk.Entry(root, width=10)
entry2.pack(pady=5)

def edit():
    entry1.config(state="normal")
    entry2.config(state="normal")

button_edit = tk.Button(root, text="edit", command=edit)
button_edit.pack(pady=10)

def clickNumb_update(event):
    global clickNumb
    clickNumb = entry1.get()
    print(clickNumb)

def interval_update(event):
    global interval
    interval = entry2.get()
    print(interval)

entry1.bind("<KeyRelease>",clickNumb_update)
entry2.bind("<KeyRelease>",interval_update)

def set_readonly(event):
    event.widget.config(state="readonly")

entry1.bind("<Return>", set_readonly)
entry2.bind("<Return>", set_readonly)

label3 = tk.Label(root, text='"]": save cords, "=": run, "[": stop')
label3.pack(pady=5)


def button1_action():
    global multiPos
    multiPos = not multiPos
    labelMP.config(text=multiPos_state())
    print(multiPos)

def multiPos_state():
    if multiPos:
        return "on"
    else:
        return "off"

def loopedClick_state():
    if loopedClick:
        return "on"
    else:
        return "off"

def button2_action():
    global loopedClick
    loopedClick = not loopedClick
    labelLC.config(text=loopedClick_state())
    print(loopedClick)


button1 = tk.Button(root, text="multi position", command=button1_action)
button1.pack(pady=10)

labelMP = tk.Label(root, text=loopedClick_state())
labelMP.pack(pady=5)

button2 = tk.Button(root, text="looped clicking", command=button2_action)
button2.pack(pady=10)

labelLC = tk.Label(root, text="off")
labelLC.pack(pady=5)


def addPos(event):
    x, y = mouse.position
    cords.append((x,y))
    print(f"saved cords: {x},{y}")
    time.sleep(0.3)
root.bind("<]>",addPos)

def startClick(event):
    global click
    click = True
    print(click)
root.bind("<=>",startClick)

def autoclicker():
    global click
    while click:
        if multiPos:
            for x,y in cords:
                mouse.position=(x,y)
                mouse.click(Button.left)
                time.sleep(float(interval))
                if not loopedClick:
                    if x >= cords[-1][-1]:
                        click = False
                if keyboard.is_pressed("["):
                    click = False
        else:
            for i in range(int(clickNumb)):
                mouse.position=cords[-1]
                mouse.click(Button.left)
                time.sleep(float(interval))
                if not loopedClick:
                    if i >= int(clickNumb)-1:
                        click = False
                if keyboard.is_pressed("["):
                    click = False
                    print(click)


    root.after(100,autoclicker)

autoclicker()
root.mainloop()
