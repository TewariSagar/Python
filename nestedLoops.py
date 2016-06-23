#multiply each element of the first list with each element of the second list

list1 = [1,2,3,4]
list2 = [4,3,2,1]

for i in list1:
	for j in list2:
		print i*j
	print i

print "break"

for i in range(10):
	if i%2 == 0:
		print i
