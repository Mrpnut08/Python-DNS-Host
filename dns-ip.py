from DNSResolver import DNSResolver
import tkinter


class DNSIPGui(tkinter.Frame):
	
	def __init__(self, master=None):
		
		self.dns_resolver = DNSResolver()
		
		### Initialize the GUI.
		tkinter.Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
	
	#~~ def __init__(self, master=None)
	
	def createWidgets(self):
	
		self.input_label = tkinter.Label(self, text = "Enter domain name:")
		self.input_label.pack()
		
		self.domain_textbox = tkinter.Entry(self)
		self.domain_textbox.pack()
		
		self.resolve_button = tkinter.Button(self, text= "Find IP addresses", command="resolver_click")
		self.resolve_button.pack()
		
		self.addresses_panel = tkinter.Frame(self,self)
		self.addresses_panel.pack()
		
		self.addresses_label = tkinter.Label(self.addresses_panel, text = "Pending domain name")
		self.addresses_label.grid(columnspan=2)
		
		self.ipv4_label = tkinter.Label(self.addresses_panel, text= "IPv4")
		self.ipv4_label.grid(row=1, column=0)
		
		self.ipv6_label = tkinter.Label(self.addresses_panel, text= "IPv6")
		self.ipv6_label.grid(row=1, column=1)
		
		self.ipv4_list = tkinter.Listbox(self.addresses_panel)
		self.ipv4_list.grid(row=2, column=0)
		
		self.ipv6_list = tkinter.Listbox(self.addresses_panel)
		self.ipv6_list.grid(row=2, column=1)
	#~~ def createWidgets(self)

#~~ class DNSIPGUI (tkinter.Frame)

root = tkinter.Tk()
app = DNSIPGui(root)
app.mainloop()
