#tuples are immutable lists whose contents can be changed after it has been created

#data is untouchable

my_tuple = ()

#create a tuple with 1 element
#we need to leave a comma for python to recognize this as a tuple otherwise it is considered integer
my_tuple = (9,)
print my_tuple

my_tuple = (1,2,3,4,5)
print my_tuple

#indexing also works with tuple

print my_tuple[1]
print my_tuple[-1]

#we can just view the tuple after it has been created. we cant add or delete


#tuple packing and unpacking. here we assign a tuple values certain parameter variables and map them to each other
#here both the number of elements both ways should be same
tuple1 = ("ciseco", "2600")
print tuple1

(vendor, model) = tuple1
print vendor 
print model

#we can also assign values this way

(a,b,c) = (1,2,3)
print a
print b
print c

