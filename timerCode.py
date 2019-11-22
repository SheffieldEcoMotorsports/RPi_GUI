# Code for timer

import tkinter as tk
from tkinter import *

class Timer:
    def __init__(self, mainWin):
        self.state = False
        self.timer = [0, 0, 0]
        self.timer2= [0, 0, 0]
        self.lap_value = 0
        self.pattern =  '{0:02d}:{1:02d}:{2:02d}'

        self.tkCanvas = tk.Canvas(mainWin, width=150, height=30)


        self.B = tk.Button(text="Start timer", command= lambda:[self.start(), self.update_timeText()], activebackground='green')
        self.B.place(relx = 0.73, rely = 0.3, anchor = CENTER)

        self.timeText = tk.Label(text="00:00:00", font=("Helvetica", 25), bg='lightgray')
        self.timeText.place(relx = 0.6, rely = 0.3, anchor = CENTER)

        #self.pauseButton = tk.Button(text = 'Pause', command = self.pause, activebackground='yellow')
        #self.pauseButton.grid(row=0,column=4)

        #self.resetButton = tk.Button(text = 'Reset', command = self.reset, activebackground='red')
        #self.resetButton.grid(row=0, column=5)

        self.globaltimeText = tk.Label(text= "00:00:00", font=("Helvetica", 25), bg='grey')
        self.globaltimeText.place(relx = 0.6, rely = 0.35, anchor = CENTER)



        ###

        # Lap incrementing

        self.lap_value_label = tk.Label (text = self.lap_value, font=("Helvetica", 25), bg='lightgray')
        self.lap_value_label.place(relx = 0.8, rely = 0.3, anchor = CENTER)

        self.lap_button = tk.Button(text= 'Increase Lap', command = self.increase, activebackground='gray')
        self.lap_button.place(relx = 0.87, rely = 0.3, anchor = CENTER)






    def increase(self):
        self.lap_value += 1
        self.lap_value_label.configure(text= self.lap_value)
        self.reset()
        ###

    def update_timeText(self):
        if self.state:
            # Every time this function is called, we will increment 1 centisecond (1/100 of a second)
            self.timer[2] += 1
            self.timer2[2] += 1
            # Every 100 centisecond is equal to 1 second

            if self.timer[2] >= 100:
                self.timer[2] = 0
                self.timer[1] += 1
            if self.timer2[2] >= 100:
                self.timer2[2] = 0
                self.timer2[1] += 1
            # Every 60 seconds is equal to 1 min
            if self.timer[1] >= 60:
                self.timer[0] += 1
                self.timer[1] = 0
            if self.timer2[1] >= 60:
                self.timer2[0] += 1
                self.timer2[1] = 0
            # We create our time string here
            self.timeString = self.pattern.format(self.timer[0], self.timer[1], self.timer[2])
            self.timeString2 = self.pattern.format(self.timer2[0], self.timer2[1], self.timer2[2])
            # Update the timeText Label box with the current time
            self.timeText.configure(text=self.timeString)
            self.globaltimeText.configure(text=self.timeString2)
            # Call the update_timeText() function after 1 centisecond
        self.timeText.after(10, self.update_timeText)
    def start(self):
        self.state = True

    # To pause the timer
    def pause(self):
        self.state = False

    # To reset the timer to 00:00:00
    def reset(self):
        self.timer = [0, 0, 0]
        self.timeText.configure(text='00:00:00')

    def grid(self, rowIn, columnIn):
        # Calls the tk grid function
        self.tkCanvas.grid(row=rowIn, column=columnIn)