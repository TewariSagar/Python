#sets can be seen as lists that dont have duplicate elements

list4 = [1,2,2,4,3]

print list4

#create a set

set1 = set(list4)
print set1
type(set1)

#another way to create a set from version 2.7 onward

set2 = {11,12,2,2,4,5,6,}

print set2

#len() can be used to print the length of set

print len(set2)

#11 in set2
print 11 in set2
print 100 in set2
print 10 not in set2

#sets are mutable

#adding an element to the set at the end

set2.add(999)

#remocving a particular element from the set

set2.remove(11)

print set2



