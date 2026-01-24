number1 = [1,2,3]
number2 = [4,5,6]
mapped = map(lambda x,y: x+y, number1,number2)
print('addition of two lists: ', list(mapped))


nums = [1,2,3,4,5]
def square(n):
    return n*n
squared = list(map(square,nums))
print('the squared values: ' , squared)