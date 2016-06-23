#len() is used to find the number of elements

tuple2 = (1,2,3)
print len(tuple2)

print min(tuple2)

print max(tuple2)

#we can also concatenate tuples

tuple3 = tuple2 + (5,6,7,8)

print tuple3

print tuple3 *3

#we can also use slicing on tuples
print tuple3[0:2]

print tuple3[::-1]

#we can also use the 'in' 'not in'

#delete the entire tuple

del tuple3
print tuple3

