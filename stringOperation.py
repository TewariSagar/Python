#.index() return the index of the first occurence of a letter

a = "Sagar"
print a.index("a")

#count returns the number of times the character appears in a string

print a.count("a")

#find returns the index of a matched string else -1

print a.find("r")
print a.find("z")

#.lower() returns the lower case of the string

#.upper() returrns the entire string in uppercase
#.startswith() returns true if the character startes with the specified character

#similar is the .endswith() method
print a.startswith("g")

#string() eliminates all the whitespaces

b = "Sagar is not a jerk     "
print b.strip()
c = "$sagar is $cute$"
#the method below removes the starting and trailing dollar sign only
print c.strip("$")

x = "Sagar$Tewari$In$Python"

#this repalces all occurences of the dollar sign with no character
print x.replace("$" , "")


#split by a delimiter

d = "this,is,python,tutorial"
print d.split(",")

#insert an underscore after every character in the string
#we can read the command like join all the characters of string p using an underscore
p = "Sagar"
print "_".join(p)


