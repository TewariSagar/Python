#the logic of break is the same as in JAVA

for i in range(10):
	print i
	if i == 7:
		break

#the continue statement makes python ignore any code below the current iteration only and goes up to the top of the for loop

list1 = [4,5,6]
list2 = [10,20,30]

for i in list1:
	for j in list2:
		if j==20:
			continue
		print i*j
	print "Outside the nested for loop"

#the pass statement is the way of telling that python that dont do anything
for i in range(10):
	pass

