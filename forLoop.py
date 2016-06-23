#this document mainly deals with the for and for else loop

vendors = ['cisco' , 'hp','nortel','avaya','juniper']
print vendors
for i in vendors:
	print i

#we can also iterate over a string
my_string = 'cisco'
for i in my_string:
	print i

 #range(5) prints all integers from 0 to 4
print range(5)

#if we dont want to start the range count from 0. Here 5 is the starting point
print range(5,10)

#range with a step increment of 2
print range(1,10,2)

#for loop using the range function
for i in range(5):
	print i

#iterate a list of vendors using the range function
for i in range(len(vendors)):
	print vendors[i]

#another way to iterate the for loop

for index, element in enumerate(vendors):
	print "Index is %d" % index
	print "Element is %s" % element
#the for else loop is used when we want to print something when the for loop has finished executing

for i in vendors:
	print i
else:
	print "the end is reached"
