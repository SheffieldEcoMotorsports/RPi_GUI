#Actual Main code

import tkinter as tk
import barGaugeCode
import meterGaugeCode
import timerCode

def updateGauges(gauges, newVals, UPDATERATE, mainWin):
    gauges[0].setVal(newVals[0])
    gauges[1].setVal(newVals[1])
    gauges[2].update_timeText()
    
    ###
    #Insert sensor functions here
    ###
    
    ###
    #EG - TBD
    newVals[0] -= 1
    newVals[1] += 0.5
    ###
    mainWin.after(UPDATERATE, lambda: updateGauges(gauges, newVals, UPDATERATE, mainWin))

mainWin = tk.Tk()
mainWin.title("Test Win")
mainWin.geometry("800x480")
mainWin.configure(bg='#0c0824')
#WINW = 800
#WINH = 800
UPDATERATE = 100#ms
STARTVALS = [100, 0]

gauges = [barGaugeCode.barGauge(mainWin),
          meterGaugeCode.Meter(mainWin, height=300, width=300),
          timerCode.Timer(mainWin)
          ]
#Initialise gauges
gauges[0].place(130, 320)
gauges[1].setrange(0, 15)
gauges[1].place(x=225, y=10)
gauges[2].place(535,125)

mainWin.after(UPDATERATE, lambda: updateGauges(gauges, STARTVALS, UPDATERATE, mainWin))
mainWin.mainloop()
