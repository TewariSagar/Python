#convert an integer to a string

num = 2
num1 = str(num)
print num1

#convert float to string

flt = 2.5
flt1 = str(flt)
print flt1

#convert string to integer but there has to be a valid conversion possible between string to integer. "s" cannot be converted to an int data type

str = "5"
number = int(str)
print number

#convert a integer to a float
integervar = 2
fltvar= float(integervar)
print fltvar

#converting tuple into a list
tup1 = (1,2,3)
list1 = list(tup1)

print list1

#convert a list to a tuple
list1 = [1,2,3,]
tup2 = tuple(list1)
print tup2

#we can use the set(list1) method to convert a list to a set

#convert between binary,decimal, hex 
num_dec = 10
num_bin = bin(num_dec)
print num_bin
num_hex = hex(num_dec)
print num_hex

num_decimal = int(num_hex,16)
print num_decimal


