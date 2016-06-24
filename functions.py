#creating a function
def my_first_function():
	"This is our first funtion" #this line is optional and is just a description for help
	print "Hello Python!"

#calling a function is just by writing its name
my_first_function()

#a function with 1 parameters. there can be multiple parameters for a function
def my_second_function(x):
	print x

my_second_function("200OK")

#function with a return statement
def my_third_function(x,y):
	sum = x+y
	return sum

my_third_function(10,1)

