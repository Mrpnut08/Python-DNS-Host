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
		
		self.resolve_button = tkinter.Button(self, text= "Find IP addresses", command= self.resolver_click)
		self.resolve_button.pack()
		
		self.addresses_panel = tkinter.Frame(self,self)
		self.addresses_panel.pack()
		
		self.addresses_label = tkinter.Label(self.addresses_panel, text = "Pending domain name")
		self.addresses_label.grid(row=0, columnspan=2)
		
		self.ipv4_label = tkinter.Label(self.addresses_panel, text= "IPv4")
		self.ipv4_label.grid(row=1, column=0)
		
		self.ipv6_label = tkinter.Label(self.addresses_panel, text= "IPv6")
		self.ipv6_label.grid(row=1, column=1)
		
		self.ipv4_list = tkinter.Listbox(self.addresses_panel)
		self.ipv4_list.grid(row=2, column=0)
		
		self.ipv6_list = tkinter.Listbox(self.addresses_panel, width= 35)
		self.ipv6_list.grid(row=2, column=1)
	#~~ def createWidgets(self)		
			
	def resolver_click(self):
		domain_name = self.domain_textbox.get()
		self.addresses_label["text"] = "IP addresses for " + domain_name
		self.dns_resolver.setDNSName(domain_name)
		self.dns_resolver.resolve()
			
		self.populateListbox(self.ipv4_list, self.dns_resolver.ipv4_addresses)
		self.populateListbox(self.ipv6_list, self.dns_resolver.ipv6_addresses)
		
	def populateListbox(self, listbox, items):
		if listbox.size() > 0:
			listbox.delete(0, listbox.size()-1)
			
		for item in items:
			listbox.insert(0, item)
	
#~~ class DNSIPGUI (tkinter.Frame)

root = tkinter.Tk()
root.wm_title("DNS/IP Looker")
app = DNSIPGui(root)
app.mainloop()
