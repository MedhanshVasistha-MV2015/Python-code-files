'''Print this test dictionary and ask the user to enter the value they want to
check the frequency (number of occurrences) in the test dictionary. Then
print the frequency of that value.'''
dict = {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print("The test dictionary is:", dict)
values = int(input("Enter the value you want to check frequency for: "))
frequency = sum(1 for value in dict.values() if value == values)
print('The frequency of ', values, 'in the dictionary is: ', frequency)