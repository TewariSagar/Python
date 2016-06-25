my_var = 10
def myFunction():
	print "this is the print statement inside the module"
#if we dont want the below print statement to be executed when this file is being used as a module in some other application
#but this print statement is executed when we execute this file independently
if __name__ == '__main__':
	print "This will still be executed"
