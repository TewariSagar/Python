#there are several kinds of python arguments
#the one we saw in the functions.py were positional arguments i.e. the number of args and the parameters should be the same

#keyword arguments allow us to ignore some of the arguments in the function parameter and even allows us to change the order

def func(x,y,z):
	sum = (x+y)*z
	print sum
func(z=3,x=1,y=1)

def secFunc(x,y,z=3):
	sum = (x+y) *z
	print sum


secFunc(1,2)

#when we call the function with  a new value of z=4, it overwrites the prev value of z=3
secFunc(1,2,4)

#if we dont know the number of arguments the function might have we use '*' to keep that as a dynamic parameter in the function. the variable with the arg is a tuple of the number of parameters with pass to the function
#the approach here is the positional argument approach

def thirdFunc(x, *args):
	print x
	print args

thirdFunc(1,2,3,4)

#we can also print the args individually and not as a tuple

def fourFunc(x, *args):
	print x
	for i in args:
		print i

fourFunc(1,2,3,4)

#handling unknown number of arguments by using keyword arguments '**'

def fiveFunc(x, **kwargs):
	print x
	print args


