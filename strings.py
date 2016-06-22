#define a string and assign it a value

my_string = "this is a test string"
print my_string

#we need triple quotes when we want to enter the string on multiple lines

my_string = """this 
... is
... my
... first"""

print my_string

my_string = """this\
... is\
... done"""

print my_string
#when counting from left to write the first letter has index 0 and so on but when counting from right to left the first index is -1, then -2 and so on
second_string = "python string"
print second_string[0]

print second_string[4]
print second_string[-1]
print second_string[-3]

#if we enter the invalid index of string we get an error

print len(second_string)

