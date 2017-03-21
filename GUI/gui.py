#!/usr/bin/python3
from tkinter import *
import subprocess
import time





def callback():
	print ("called the callback!")

def loadFile():
	print ("load")

def runPrograms():
	process = subprocess.Popen("./wait.sh", shell=True, stdout=subprocess.PIPE)
	while process.poll() is None:
		time.sleep(1)
		print("waiting")

def close_window():
	root.destroy()


root = Tk()
window = Frame(root)
buttons = Frame(window)
labels = Frame(window, height=1, bd=1)
L = []
lStatus = []

loadButton = Button(buttons, text="open", width=6, command=loadFile)
runButton = Button(buttons, text="run", width=6, command=runPrograms)
quitButton = Button(buttons, text="quit", width=6, command=close_window)

L.append(Label(labels, text="Exorcism1:").grid(column=0,row=0))
lStatus.append(Label(labels, text="...").grid(column=1,row=0))
L.append(Label(labels, text="Exorcism2:").grid(column=0,row=1))
lStatus.append(Label(labels, text="...").grid(column=1,row=1))
L.append(Label(labels, text="Exorcism3:").grid(column=0,row=2))
lStatus.append(Label(labels, text="...").grid(column=1,row=2))
L.append(Label(labels, text="Exorcism4:").grid(column=0,row=3))
lStatus.append(Label(labels, text="...").grid(column=1,row=3))

loadButton.pack(side=LEFT, padx=2, pady=2)
runButton.pack(side=LEFT, padx=2, pady=2)
quitButton.pack(side=LEFT, padx=2, pady=2)
buttons.pack(side = TOP, fill=X)
labels.pack(side=BOTTOM, fill=X, padx=75, pady=2)
window.pack()
root.mainloop()



		

# for i in range(0, 3):
# 	L[i].pack( padx=0, pady=2)
# 	lStatus[i].pack(  padx=0, pady=2)




