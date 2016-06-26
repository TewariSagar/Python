#python also has an object oriented approach of programming
#class is a datatype which has its own variables, methods. it is like a blueprint for creating objects and object is an instance of a defined class

#inheritance is that a new class can inherit all the names and functionalities from an existing class

#define a class and the class name is in camel case

class MyRouter(object):
	#here comes the class content
	'''this is a class that describes a router'''
	#init method is called the class constructor like java constructor
	def __init__(self, routername, model, serialno, ios):
		#self is like this(??? THIS MIGHT BE INCORREC)
		#self points to the current instance of the class
		self.routername = routername
		self.model = model
		self.serialno = serialno
		self.ios = ios
	def print_router(self, manuf_data):
		#every function we define we need to add the self parameter
		print "the router name is: ", self.routername
		print "the router model is: ", self.model
	
#creating object
router1 = MyRouter("R1", "2600", "1234556", "12.4")
print router1.model
router1.print_router(2016)

#we can also set the attribute of an object or get the attribute of an object

print getattr(router1, "model")
setattr(router1, "ios", "sagarIOS")
print getattr(router1, "ios")

#we can also use the hasattr() attribute

print hasattr(router1, "ios")
