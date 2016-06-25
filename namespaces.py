#NAMESPACES ARE PLACES WHERE WE DEFINE NAMES FOR OUR VARIABLES, FUNCTIONS, CLASSES ETC. 
#THERE CAN BE SAME NAME IN DIFFERENT NAMESPACES
#THERE ARE TYPES OF NAMES DEPENDING ON THE NAMESPACE THEY BELONG TO

#1. BUILT-IN FUNCTIONS
#LEN() MAX() MIN() RANGE()
#2. GLOBAL NAMESPACE IS THE NAMESPACE WITH GLOBAL VAR NAMES
#3. LOCAL IS LIKE THE LOCAL VARIABLES IN A FUNCTION

#range belongs to built in namespace
print range(10)

#global namespace

var = 10
print var

#local namespace
def myfunc():
	#local namespace
	var = 5
	print var

myfunc()
#global namespace
print var

#USE A GLOBAL VARIABLE IN  A LOCAL NAMESPACE IS DONE USING THE GLOBAL KEYWORD

glob_var = "this is global"

def printfunc():
	global glob_var
	print glob_var

printfunc()

#return a local variable to be used in global scope

def function():
	x = 10
	print x
	return x

new_x = function()
print "%d is the value of new_x " %new_x
