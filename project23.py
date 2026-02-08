'''1. Take a number from the user, create a list with all the odd numbers under
the input value and another list of odd numbers.
2. Create a list of fruits. Then, convert the first letter of every element to
capital and create a new list of updated values.'''

num = int(input("Enter a number: "))

odd_numbers = [i for i in range(1, num) if i % 2 != 0]
even_numbers = [i for i in range(1, num) if i % 2 == 0]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)


fruits = ["apple", "banana", "mango", "grapes"]

capital = {
    'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E',
    'f':'F', 'g':'G', 'h':'H', 'i':'I', 'j':'J',
    'k':'K', 'l':'L', 'm':'M', 'n':'N', 'o':'O',
    'p':'P', 'q':'Q', 'r':'R', 's':'S', 't':'T',
    'u':'U', 'v':'V', 'w':'W', 'x':'X', 'y':'Y'
}

fruits = ["apple", "banana", "mango", "grapes"]

new_fruits = [capital[fruit[0]] + fruit[1:] for fruit in fruits]

print("Original list:", fruits)
print("Updated list:", new_fruits)
