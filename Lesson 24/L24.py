'''Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]'''
setint = {10,20,30,40,50}
print(setint)
mixset = {7 , 'Dog' , 1.3 , False}
print(mixset)
set1 = {1,2,3,4,3,2}
print(set1)
list1 = [1,2,3,2]
setlist = list1
print(setlist)
setremove = {0,1,3,4,5}
setremove.pop()
print(setremove)
