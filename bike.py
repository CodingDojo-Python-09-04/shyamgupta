class Bike(object):
	def __init__(self,price,max_speed,miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
	def displayinfo(self):
		print "Price of the bike is {}".format(self.price)
		print "Maximum speed is {}".format(self.max_speed)
		print "Total miles travelled is {}".format(self.miles)
		return self
	def ride(self):
		print "Riding"
		self.miles += 10
		print "Miles travelled is {}".format(self.miles)
		return self
	def reverse(self):
		if self.miles<=0:
			self.miles = 0
			print "Miles travelled is {}".format(self.miles)
		else:
			print "Reversing"
			self.miles -= 5
			print "Miles travelled is {}".format(self.miles)
		return self

bike1 = Bike(10000,80)
bike2 = Bike(15000,90)
bike3 = Bike(20000,100)

print "Printing info for bike 1"
bike1.ride().ride().ride().reverse().displayinfo()
print "Printing info for bike 2"
bike2.ride().ride().reverse().reverse().displayinfo()
print "Printing info for bike 3"
bike3.reverse().reverse().reverse().displayinfo()





