'''Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple'''
tupled = (3, 'three' , False )
print('The tuple with different datatypes is: ', tupled)
tupleint = (10,20,30,40)
print('The tuple with integers is: ' , tupleint)
tuplenine = tupleint + (9,)
print('The tuple that added 9 to the previous tuple is: ' , tuplenine)
tuplelen = (1,1,1,2)
count = tuplelen.count(1)
print('The occurences of 1 in tuplelen is: ' , count)
tupleslice = (0,2,4,6,8,10,12,14)
slice = tupleslice[0:11]
print('The tuple that is sliced is: ' , slice)