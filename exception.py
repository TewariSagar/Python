#this doc is about exception handling
#we have a try block with 1 level of inendation where we put code we believe cam raise an error

#except block is like the catch block in JAVA. if our except code is not the correct way to handle exception, out code wont work

for i in range(10):
	try:
		print i / 0
	except ZeroDivisionError:
		print "Division by 0 not allowed"
#it is also better to raise exception with proper clauses to know which operation raised an exception

#else clause after try is executed when no exception is raised

try:
	print 4/2
except ZeroDivisonError:
	print "Divison by 0 not allowed"
else:
	print "the end has been reached"

#finally is used to print anything whether an exception was raised or not
#finally clause is always executed
	
	
