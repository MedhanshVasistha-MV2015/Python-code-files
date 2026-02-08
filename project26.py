
'''Rose is a computer science student who wants to know the product of the
values being passed in a tuple. Write a Python program to calculate the
product, multiplying all the numbers of the given tuple.

1. tup1 = (4, 3, 2, 2, -1, 18)
2. tup2 = (2, 4, 8, 8, 3, 2, 9).'''
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)
tupx  = tup1 + tup2
product = 1
for i in tupx:
    product *= i
print(product)