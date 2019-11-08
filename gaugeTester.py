#Actual Main code

import tkinter as tk
import barGaugeCode
import meterGaugeCode

def updateGauges(gauges, newVals, UPDATERATE, mainWin):
    for i in range(len(gauges)):
        gauges[i].setVal(newVals[i])
    ###
    #Insert sensor functions here
    ###
    
    ###
    #EG - TBD
    newVals[0] -= 2
    newVals[1] += 0.5
    ###
    mainWin.after(UPDATERATE, lambda: updateGauges(gauges, newVals, UPDATERATE, mainWin))

mainWin = tk.Tk()
mainWin.title("Test Win")
mainWin.geometry("800x800")
WINW = 800
WINH = 800
UPDATERATE = 100#ms

gauges = [barGaugeCode.barGauge(mainWin),
          meterGaugeCode.Meter(mainWin, height=300, width=300)]

gauges[0].grid(0, 0)
gauges[1].setrange(0, 30)
gauges[1].grid(row=0, column=1)

mainWin.after(UPDATERATE, lambda: updateGauges(gauges, [100, 0], UPDATERATE, mainWin))
mainWin.mainloop()
