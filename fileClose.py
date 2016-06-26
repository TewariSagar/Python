#it is always recommended to close after using the open() method to avoid any OS process issues


#.closed() method is used to check if the file is closed or not

# print newfile.closed()

#there is another way that ensures that the open file is automatically closed and was introduced in python V2.5 onward

#the 'f' here is the file object
with open('pythonTest.txt', 'w') as f:
	f.write("hello python\n")

print f
