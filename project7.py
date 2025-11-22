'''Raj is a class teacher of grade 10. He wants to design a program that only
allows students aged 10 to 20 years in his class. As a result, students whose
age is more than 20 can not enrol in his class.
Best of luck.'''
age = int(input("Enter your age: "))
if age >= 10 and age <= 20:
    print("You are eligible to enroll in the class.")
else:
    print("You are not eligible to enroll in the class.")
