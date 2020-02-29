import tkinter as tk
import subprocess
import os 

root= tk.Tk()

mainCanvas = tk.Canvas(root, width = 400, height = 300)
mainCanvas.pack()

inputEntry = tk.Entry (root) 
mainCanvas.create_window(200, 140, window=inputEntry)

def getSquareRoot ():
    try:  
        app_id = inputEntry.get()
        #Replace with own path
        idlePath = f"C:/Users/mepps/pictures/IdleMatsterFiles/idle_master_extended_v1.4/steam-idle.exe {app_id}"
        os.system(idlePath)
    except:
        print('Something fricked up')
    
    

    
button1 = tk.Button(text='Enter App ID', command=getSquareRoot)
mainCanvas.create_window(200, 180, window=button1)

root.mainloop()