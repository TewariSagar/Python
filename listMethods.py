#max() minimum() functions in a list

list = ["cisco", "HP", 10,10.5,-11]
print min(list)
print max(list)

#python always considers strings to be maximum than numbers

print max(1,"a")
#add the element to the end of the list

list.append(100)

print list

#del function removes the index at the specified index

del list[4]
print list

#remove function removes the element specified by name

list.remove("HP")

#insert function is used to insert a specific element at the specific index

list.insert(2,"ElementAtTwo")

print list
#the extend() method is used to append the second list after the first list

list2 = [1,11,111]
list.extend(list2)

print list

#the .index() method is used to get the index of the specified element

print list.index("cisco")

#count function is used to return the number of occurences of an element

list.count(10)

#sort() function by default sorts the list in increasing order

list2.append(100)
list2.append(60)

list2.sort
print list2

#if we want to print the list in reverse order

list2.reverse()

#if we want to sort the elements of the list and create a new list at the same time

sorted(list2)
#this is used to reverse the list
sorted(list2, reevrse = True)

#we can also add, multiply lists and the duplicate elements are allowed
