#whenever we want to use regular expression always import the re module

# import re
#python provides 4 different regex functions

import re
var = "This is a beautiful day. I have raju mama sitting next to me. He is searching for an apartment on a god knows what website."

#the syntax for using the match function is as follows

# a = re.match(pattern, string, opetional flags)
#here a is the match object

#check if the string starts with "This"

a = re.match("This" ,var)
print a

#if we want to return the match found according to the pattern we used
print a.group()

#if we want to find the match ignoring the case
x = re.match("this", var, re.I)
print x.group()

#search function is used to search for a pattern in the entire string unlike the match function that only searches the beginning of the string

y = re.search("raju", var, re.I)
print y.group()

#SOME REGEX RULES
# () - brackets represents a group
# . - represents any character
# + - looks for 1 or more repeating character specified by the preceeding character
# \d - represents any single decimal digit from 0 to 9
# \s - represents any match to the whitespace
# {2,} - represents that python should expect two occurences of any character preceeding the curly bracket
#  \w - represents the search for any alphabet character from A to Z a-z 0-9
# r - means that the string should be treated as raw
# * - looks for 0 or more repeating character

#the findall() returns a list where each element is a pattern matched in the target string
#returns a list of all the matched patters

arp = "22.22.22.1      0    b4:a9:5a VLAN#222    L"
print re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)


