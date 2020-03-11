# Code for timer

import tkinter as tk
import time

import math

def secToFormat(timeChange):
    #Format seconds to min/sec/millisec
    milliChange = str((timeChange%1) * 100)[:2]#first 2 digits of milli
    #This is needed because sometimes it will be a single digit so it has a '.'
    if "." in milliChange:
        milliChange = milliChange[0]
    #Round down
    intTimeChange = math.floor(timeChange)
    #means it wont go over 60 eg 67 -> 7, 40 -> 40 etc
    secChange = str(intTimeChange%60)
    #Integer division so it is in whole minutes eg 130 -> 2
    minChange = str(intTimeChange//60)
    #Format so always 2 digits eg 04 not 4
    if int(milliChange) < 10:
        milliChange = ":0" + milliChange
    else:
        milliChange = ":" + milliChange
    if int(secChange) < 10:
        secChange = ":0" + secChange
    else:
        secChange = ":" + secChange
    if int(minChange) < 10:
        minChange = "0" + minChange

    FulltimeString = minChange + secChange + milliChange
    return FulltimeString


class Timer:
    def __init__(self, mainWin):
        self.state = False
        self.startTime = 0
        self.lap_value = 0
        self.lapTime = 0

        self.tkCanvas = tk.Canvas(mainWin, width=300, height=100, bg='#0c0824',highlightthickness=0)


        self.B = tk.Button(self.tkCanvas, text="Start timer", command= lambda:[self.start(), self.update_timeText()], activebackground='green')
        self.B.place(x=140, y=0)

        self.timeText = tk.Label(self.tkCanvas, text="00:00:00", font=("Helvetica", 25), bg='lightgray')
        self.timeText.place(x=0, y=0)

        self.globaltimeText = tk.Label(self.tkCanvas, text= "00:00:00", font=("Helvetica", 25), bg='grey')
        self.globaltimeText.place(x=0, y=50)



        ###

        # Lap incrementing

        self.lap_value_label = tk.Label (self.tkCanvas, text = "Laps: 0", font=("Helvetica", 25), bg='lightgray')
        self.lap_value_label.place(x=140, y=25)

        self.lap_button = tk.Button(self.tkCanvas, text= 'Increase Lap', command = self.increase, activebackground='gray')
        self.lap_button.place(x=140, y=70)






    def increase(self):
        self.lap_value += 1
        lapText = "Laps: " + str(self.lap_value)
        self.lap_value_label.configure(text=lapText)
        self.reset()
        ###

    def update_timeText(self):
        if self.state:
            #Store time so both timers are in sync
            currentTime = time.time()

            #Time is the difference between now and when it started
            timeChange = currentTime - self.lapTime
            self.timeText.configure( text=secToFormat(timeChange) )
            
            timeChange = currentTime - self.startTime
            self.globaltimeText.configure( text=secToFormat(timeChange) )

    def start(self):
        self.state = True
        self.startTime = time.time()
        self.lapTime = self.startTime

    def reset(self):
        #Set lap time to the current time
        self.lapTime = time.time()
        self.timeText.configure(text='00:00:00')

    def place(self, xIn, yIn):
        # Calls the tk place function
        self.tkCanvas.place(x=xIn, y=yIn)
