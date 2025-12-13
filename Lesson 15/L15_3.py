def add (p , q):
    return p + q
def subtract (p , q):
    return p - q
def multiply (p , q):
    return p * q
def divide (p , q):
    return p / q
print('Select the operation you want to perform: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide')
op = input('Enter choice (1/2/3/4): ') 
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
if op == '1':
    print(n1 , '+' , n2 , '=' , add (n1 , n2))
elif op == '1':
    print(n1 , '-' , n2 , '=' , subtract (n1 , n2))
elif op == '1':
    print(n1 , '*' , n2 , '=' , multiply (n1 , n2))
elif op == '1':
    print(n1 , '/' , n2 , '=' , divide (n1 , n2))
else:
    print('Invalid input')
