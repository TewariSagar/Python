dict1 = {"vendor" : "cisco", "model" : "2004", "ports" : "4"}
print dict1

#retrieve value corresponding to a key
print dict1["vendor"]

#add a new key value pair to the dictionary

dict1["RAM"] = "128"

print dict1
#if we want to change the value corresponding to a key

dict1["vendor"] = "netgear"

print dict1

#we can also delete the key value pair by using the del function

del dict1["vendor"]
print dict1

#we can use the len() to find the number of key value pairs

#we can also search if a key is present in the dictionary

print len(dict1)
print "RAM" in dict1

#print a list of all keys in the dictionary

print dict1.keys()

#print a list of all values 

print dict1.values()

#print a list of tuples each tuple containing a key value pair

print dict1.items()


