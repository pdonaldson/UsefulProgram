import ctypes
from tkinter import *

global startX
global startY
global user32
global windowSizeX
global windowSizeY
global jump

jump = 10
windowSizeX = 200
windowSizeY = 80

user32 = ctypes.windll.user32
# get screen resolution of primary monitor
res = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
# res is (2293, 960) for 3440x1440 display at 150% scaling
user32.SetProcessDPIAware()

startX = user32.GetSystemMetrics(0)/2
startY = user32.GetSystemMetrics(1)/2
print(startX, startY)

window = Tk()
window.overrideredirect(1)
window.wm_attributes("-topmost", 1)
window.geometry("%dx%d+%d+%d" % (windowSizeX, windowSizeY, startX, startY))

text_var = StringVar(window)
text_var.set("Click to Close")

def mouseClick( event ):
    global windowSizeX
    global windowSizeY
    global startX
    global startY
    global jump

    screenX = user32.GetSystemMetrics(0)
    screenY = user32.GetSystemMetrics(1)
    startY = screenY/2
    startX = screenX/2

    handle = user32.FindWindowW(0, u'tk')
    user32.MoveWindow(handle, int(startX), int(startY), windowSizeX, windowSizeY, True)
    text_var.set('I lied :C')

def motion(event):
    text_var.set("Click to Close")
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

    global windowSizeX
    global windowSizeY
    global startX
    global startY
    global jump

    handle = user32.FindWindowW(0, u'tk')

    moveX = (x-(windowSizeX/2))
    moveY = (y-(windowSizeY/2))

    moveX = moveX/(windowSizeX/2)
    print("x:")
    print(moveX)
    moveY = moveY/(windowSizeY/2)
    print("y:")
    print(moveY)

    startX = startX - moveX*10
    startY = startY - moveY*10

    screenX = user32.GetSystemMetrics(0)
    screenY = user32.GetSystemMetrics(1)
    if startX < 0 or startY < 0 or startX > screenX - 100 or startY > screenY - 100:
        startY = screenY/2
        startX = screenX/2

    user32.MoveWindow(handle, int(startX), int(startY), windowSizeX, windowSizeY, True)

label = Label( window, textvariable=text_var, width=12, height=1)
label.place(relx=0.5, rely=0.5, anchor=CENTER)
label.bind( "<Button>", mouseClick )

window.bind('<Motion>', motion)

window.mainloop()
