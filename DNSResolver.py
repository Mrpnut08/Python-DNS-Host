import subprocess

class DNSResolver:
	
	def __init__(self, dns_name=None):
		"""Class constructor initializes the instance variables."""
		
		self.dns_name = dns_name
		self.ipv4_addresses = []
		self.ipv6_addresses = []
		
	#~~ def __init__(self, dns_name=None)
		
	def setDNSName(self, name):
		
		self.dns_name = name
		del self.ipv4_addresses[:]
		del self.ipv6_addresses[:]
	
	#~~ def setDNSNamer(self, name)
	
	def resolve(self):
		"""Resolves the dns_name and stores the addresses."""
		
		raw_result = subprocess.check_output(["host",self.dns_name])
		
		for line in raw_result.split(b'\n'):

			address = line[(line.rfind(b' ') + 1):].decode("utf-8")
			
			if b'has address' in line:
				self.ipv4_addresses.append(address)
			
			elif b'has IPv6 address' in line:	
				self.ipv6_addresses.append(address)
		#~~ for line in raw.result.split(b'\n')
		 
#~~ class DNS Resolver
