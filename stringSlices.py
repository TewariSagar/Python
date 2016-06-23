#allow us to extract various parts of the string
x = "sagartewari"

#this command gives the substring starting at the index before column and ending at index after colein but not including it

print x[1:4]

#if we dont give the second paramter after colen we get the string starting at the first index and till the end of string

#we include negative indexes if we are traversing from right to left

#if we would like to skip every second character when we are slicing

print x[::2]
#this string will have of indexes 0,2,4 and so on

#print the string in reverse order

print x[::-1]
