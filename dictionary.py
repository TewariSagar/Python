#dictionaries store data in the key value pair format
#data is usually stored in the form Vendor : cisco, Model:2600

#create an empty dictionary

dict1 = {}

print dict1

#the keys in this case are strings but we can have other datatypes as keys too
dict1 = {"vendor" : "cisco", "model" : "2600", "ports" : "4"}
print dict1

#once we store values in the dictionary their order of retrieval is randomized

#each key in the dictionary is unique and can only have string, int, tuples --- IMPORTANT
#whereas the values dont need to be unique and can be of mutable or immutable data type

