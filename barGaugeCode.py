#Code for bar Gauge

import tkinter as tk

class barGauge():
    def __init__(self, mainWin):
        self.gaugeVal = 0  #Actual value
        self.GAUGEH = 100
        self.GAUGEW = 480  #Set dimensions
        self.MAXVAL = 100  #Highest value on the gauge
        
        #Creates the tk objects
        self.tkCanvas = tk.Canvas(mainWin, width=self.GAUGEW+10, height=self.GAUGEH)
        #self.tkCanvas.pack()
        
        #Actual varying rectangle
        self.gaugeRect = self.tkCanvas.create_rectangle(0, 0, self.GAUGEW, self.GAUGEH, fill="green")
        
        #Frame of the gauge (border and markers)
        self.gaugeFrame = self.tkCanvas.create_rectangle(2, 3, self.GAUGEW, self.GAUGEH, outline="black", width=3)
        self.halfLine = self.tkCanvas.create_line(self.GAUGEW/2, self.GAUGEH-20, self.GAUGEW/2, self.GAUGEH, width=3)
        self.quaterLine = self.tkCanvas.create_line(3*self.GAUGEW/4, self.GAUGEH-10, 3*self.GAUGEW/4, self.GAUGEH, width=3)
        self.threeQuarterLine = self.tkCanvas.create_line(self.GAUGEW/4, self.GAUGEH-10, self.GAUGEW/4, self.GAUGEH, width=3)
        
        #Text to show percentage
        self.gaugeText = tk.Label(self.tkCanvas, text="100%")
        self.gaugeText.place(x=20, y=35)
        
    def setVal(self, newVal):
        self.gaugleVal = newVal
        if self.gaugeVal > self.MAXVAL:
            self.gaugeVal = self.MAXVAL
        x0,y0,x1,y1 = self.tkCanvas.coords(self.gaugeRect)
        x1 = self.GAUGEW * ( self.gaugleVal / self.MAXVAL )  #Keeps the bar in proportion with the max val and the max width
        self.tkCanvas.coords(self.gaugeRect, x0, y0, x1, y1)
        #Change coords of rectangle corners (so it moves down)
        self.gaugeText.configure(text= (str(round(newVal*100/self.MAXVAL, 2)) + "%\nBattery") )
        #Change text to show %
        if newVal/self.MAXVAL < 0.5:
            if newVal/self.MAXVAL < 0.25:
                self.tkCanvas.itemconfigure(self.gaugeRect, fill="red")
            else:
                self.tkCanvas.itemconfigure(self.gaugeRect, fill="yellow")
        #Change colour based on value
    
    def place(self, xIn, yIn):
        #Calls the tk grid function
        self.tkCanvas.place(x=xIn, y=yIn)