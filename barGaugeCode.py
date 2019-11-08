#Code for bar Gauge

import tkinter as tk

class barGauge():
    def __init__(self, mainWin):
        self.gaugeVal = 0 #Actual value
        self.GAUGEH = 480
        self.GAUGEW = 100  #Set dimensions
        self.MAXVAL = 100
        
        #Creates the tk objects
        self.tkCanvas = tk.Canvas(mainWin, width=self.GAUGEW+10, height=self.GAUGEH)
        self.tkCanvas.pack()
        
        #Actual varying rectangle
        self.gaugeRect = self.tkCanvas.create_rectangle(0, self.GAUGEH-self.gaugeVal, self.GAUGEW, self.GAUGEH, fill="green")
        
        #Frame of the gauge (border and markers)
        self.gaugeFrame = self.tkCanvas.create_rectangle(2, 3, self.GAUGEW, self.GAUGEH, outline="black", width=3)
        self.halfLine = self.tkCanvas.create_line(0, self.GAUGEH/2, 20, self.GAUGEH/2, width=3)
        self.quaterLine = self.tkCanvas.create_line(0, 3*self.GAUGEH/4, 10, 3*self.GAUGEH/4, width=3)
        self.threeQuarterLine = self.tkCanvas.create_line(0, self.GAUGEH/4, 10, self.GAUGEH/4, width=3)
        
        
    def setVal(self, newVal):
        self.gaugleVal = newVal
        if self.gaugeVal > self.MAXVAL:
            self.gaugeVal = self.MAXVAL
        x0,y0,x1,y1 = self.tkCanvas.coords(self.gaugeRect)
        y0 = self.GAUGEH * (1 - ( self.gaugleVal / self.MAXVAL ))  #Keeps the bar in proportion with the max val and the max height
        self.tkCanvas.coords(self.gaugeRect, x0, y0, x1, y1)
        #Change coords of rectangle corners (so it moves down)
    
    def grid(self, rowIn, columnIn):
        #Calls the tk grid function
        self.tkCanvas.grid(row=rowIn, column=columnIn)