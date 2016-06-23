#lists are mutable that is it can be modified after creation

list = []
print list

#add elements to the list of any data type

list = ["ciseco", 10, -1, "sagar"]

print list
print len(list)

#return the first element of the list

print list[0]

#show that the list is immutable by changing first element

list[0] = "new element"

print list
