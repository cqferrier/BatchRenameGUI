from powershellclass import PowerShell

from tkinter import filedialog

#defines a messagebox function to tell user what file to get
def messagebox(displayinfo):
	"""Presents a messagebox telling the user to select a file"""
	from tkinter import messagebox
	messagebox.showinfo(message = displayinfo)

#defines a simpledialog user friendly string entry window fxn
def dataentry(title, question):
	"""Presents a dialog box asking the user a question"""
	from tkinter import simpledialog
	userinput = simpledialog.askstring(title, question)
	return userinput
	
#asks for directory of files to be renamed
messagebox("Select the folder that contains the files you want to rename")
userdir = filedialog.askdirectory(title = "Select directory")

#asks for the current prefix of the files (e.g. sagT1MPRAGE)
prefix = dataentry('File Prefix', 'Enter the file prefix of the files you want to rename (e.g. sagT1MPRAGE)')

#asks for what the user wants to rename the files
newname = dataentry('New name', 'What would you like to rename the files?')

command = PowerShell(userdir, prefix, newname)

command.runpowershell()

