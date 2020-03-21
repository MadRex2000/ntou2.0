class Posts():
	def __init__(self, text, post_method, status):
		self.text = text
		self.post_method = post_method
		self.status = status
		self.owners = []
	def setOwners(self, owners):
		self.owners = owners

def initialize():
	global inspectors, posts
	inspectors = []
	posts = {}

