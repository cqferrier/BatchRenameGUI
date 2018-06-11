class PowerShell():
	"""A class that runs a powershell command requiring multiple args"""
	
	def __init__(self, path, currentname, requestedname):
		"""Intializes attributes of PowerShell"""
		self.path = path
		self.currentname = currentname
		self.requestedname = requestedname
		
	def changepowershellpath(self):
		"""Changes the current directory in powershell so that the command can be run"""
		import subprocess
		subprocess.Popen('powershell.exe [cd' + " " + self.path)
	
	def runpowershell(self):
		"""Uses user input of currentname, requestedname, and path to run powershell cmd"""
		import subprocess
		subprocess.Popen(["powershell", "cd " +  self.path + '; get-childitem | foreach' + 
		' { rename-item $_ $_.Name.Replace' + '("'
		+ self.currentname + '", ' + '"' + self.requestedname
		+ '"' + ") }"])	
		
