import tkinter

class DNSIPGui(tkinter.Frame):
	
	def __init__(self, master=None):
		
		### Initialize the GUI.
		tkinter.Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
	
	#~~ def __init__(self, master=None)
	
	def createWidgets(self):
	
		self.input_label = tkinter.Label(self, text = "Enter domain name:")
		self.input_label.pack(side = "top")
	#~~ def createWidgets(self)

#~~ class DNSIPGUI (tkinter.Frame)

root = tkinter.Tk()
app = DNSIPGui(root)
app.mainloop()
