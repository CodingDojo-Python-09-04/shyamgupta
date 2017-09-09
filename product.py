class Product(object):
	def __init__(self,price,name,weight,brand,cost,status="For Sale"):
		self.price = price
		self.name = name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = status
	def sell(self):
		self.status = "Sold"
		return self
	def add_tax(self,tax):
		self.price += (self.price)*tax
		return self
	def Return(self,reason):
		if reason == "Defective":
			self.status = "Defective"
			self.price = 0
		elif reason == "Box":
			self.status = "For Sale"
		elif reason == "Open":
			self.status = "Used"
			self.price -= (self.price)*0.2
		return self
	def display_info(self):
		print "Price is ${}".format(self.price)
		print "Product name is {}".format(self.name)
		print "Product weight is {}lb".format(self.weight)
		print "Product brand is {}".format(self.brand)
		print "Product cost is ${}".format(self.cost)
		print "Product Status is {}".format(self.status)

jeans = Product(20,"Blue Jeans",3,"Levi's",15)
jeans.display_info()
jeans.sell()
jeans.add_tax(0.15)
jeans.display_info()
jeans.Return("Box")
jeans.display_info()

		