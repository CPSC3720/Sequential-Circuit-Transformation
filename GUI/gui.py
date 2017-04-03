	#!/usr/bin/python3
	from tkinter import *
	import time
	import sys
	import os
	from subprocess import call
	from tkinter import ttk
	from tkinter.filedialog import *

	class GUIClass:
		def __init__(self, master):
			self.master = master
			master.title("Sequential-Circuit-Transformation")
			master.minsize(width=875, height=225)
			master.maxsize(height=301)
			self.window = Frame(root)
			self.T = Frame(self.window)
			self.labels = Frame(self.window)
			self.Clabels = Frame(self.window)
			self.buttons = Frame(root)
			self.Input =StringVar()
			self.Input.set("/CurrentInputDir/")
			self.Mod =StringVar()
			self.Mod.set("Ready")
			self.Convert =StringVar()
			self.Convert.set("Ready")
			self.EXOR =StringVar()
			self.EXOR.set("Ready")
			self.Metrics =StringVar()
			self.Metrics.set("Ready")
			Label(self.T,text="Currently working on: ", font=("Helvetica", 20, "bold")).pack()
			Label(self.labels,text="Adding modified states to file -", font=("Helvetica", 14)).pack(fill=X, padx=40)
			Label(self.labels,text="Converting file from Kiss2 to pla -", font=("Helvetica", 14)).pack(fill=X, padx=40)
			Label(self.labels,text="Running file through exorcism -", font=("Helvetica", 14)).pack(fill=X, padx=40)
			Label(self.labels,text="Gathering metrics from cubed synthesis -", font=("Helvetica", 14)).pack(fill=X, padx=40)
			Label(self.Clabels,textvariable=self.Mod, font=("Helvetica", 14)).pack( fill=X, padx=40)
			Label(self.Clabels,textvariable=self.Convert, font=("Helvetica", 14)).pack( fill=X, padx=40)
			Label(self.Clabels,textvariable=self.EXOR, font=("Helvetica", 14)).pack( fill=X, padx=40)
			Label(self.Clabels,textvariable=self.Metrics, font=("Helvetica", 14)).pack( fill=X, padx=40)
			self.LinDir = Label(self.buttons,textvariable=self.Input, font=("Helvetica", 14)).pack(side=LEFT, padx=100)
			Button(self.buttons, text="Exit",  font=("Helvetica", 14),width=10, command=self.close_window).pack(side=RIGHT, padx=5)
			Button(self.buttons, text="Run all files",  font=("Helvetica", 14),width=10, command=self.runScrips).pack(side=RIGHT, padx=5)	
			Button(self.buttons, text="Open Input Dir",  font=("Helvetica", 14), width=12, command=self.browsefunc).pack(side=RIGHT,padx=5)
			self.T.pack(side=TOP, fill=X) 
			self.labels.pack(side=LEFT, fill=X)
			self.Clabels.pack(side=RIGHT, fill=X)
			
			self.window.pack() 	
			self.buttons.pack(fill=X)

		def close_window(self):
			self.master.destroy()
		
		def browsefunc(self):
			filename = askdirectory() 
			self.Input.set(filename)
			
		def runScrips(self):
			ESOP_EXT = ".esop"
			KISS2_EXT = ".kiss2"
			PLA_EXT = ".pla"
			TXT_EXT = ".txt"
			OUTPUT_1 = "outputs/step1_Kiss2ToKiss2XOR/"
			OUTPUT_2 = "outputs/step2_Kiss2XORToPLA/"
			OUTPUT_3 = "outputs/step3_PLAToESOP/"
			OUTPUT_4="outputs/step4_metrics/"
			self.Mod.set("Working")
			for filename in os.listdir(self.Input.get()):
				if filename.endswith(".kiss2"):

					tempPath = os.path.split(filename)[1]
					inputFileNameWithExtensionRemoved = os.path.splitext(tempPath)[0]

					## First, we convert the input kiss2 file to kiss2 with modified states
					call("python KissToKiss_XOR.py %s" %
						self.Input.get() + "/" + filename, shell = True)
					continue
				else:
					continue
			self.Mod.set("Finished")
			self.Convert.set("Working")
			for filename in os.listdir(self.Input.get()):
				if filename.endswith(".kiss2"):

					tempPath = os.path.split(filename)[1]
					inputFileNameWithExtensionRemoved = os.path.splitext(tempPath)[0]

					## Second, we convert the modified kiss2 file to .pla
					call("python KissToPLA.py %s %s" %
						(inputFileNameWithExtensionRemoved + KISS2_EXT, inputFileNameWithExtensionRemoved), shell = True)
					continue
				else:
					continue
			self.Convert.set("Finished")
			self.EXOR.set("Working")
			for filename in os.listdir(self.Input.get()):
				if filename.endswith(".kiss2"):

					tempPath = os.path.split(filename)[1]
					inputFileNameWithExtensionRemoved = os.path.splitext(tempPath)[0]

					## Third, pass .pla file through exorcism_org
					call("./exorcism_org %s" %
						inputFileNameWithExtensionRemoved + PLA_EXT, shell = True)
					continue
				else:
					continue
			self.EXOR.set("Finished")
			self.Metrics.set("Working")
			for filename in os.listdir(self.Input.get()):
				if filename.endswith(".kiss2"):		
					## Note: the .esop file is consumed by the shared cube synthesis program, so we make a
					## copy of the file to the OUTPUT_3 folder in this step.
					call("cp " + inputFileNameWithExtensionRemoved + ESOP_EXT + " " + OUTPUT_3, shell = True)

					# Fourth, call shared cubed synthesis program and output to a metrics text file
					call("./GetGateCount.sh %s" % inputFileNameWithExtensionRemoved + ESOP_EXT, shell = True)

					## Move intermediate files to outputs folder,
					call("mv " + inputFileNameWithExtensionRemoved + KISS2_EXT + " " + OUTPUT_1, shell = True)
					call("mv " + inputFileNameWithExtensionRemoved + PLA_EXT + " " + OUTPUT_2, shell = True)
					call("mv " + inputFileNameWithExtensionRemoved + TXT_EXT + " " + OUTPUT_4, shell = True)

					continue
				else:
					continue
			self.Metrics.set("Finished")



	root = Tk()
	GUI = GUIClass(root)
	root.mainloop()



