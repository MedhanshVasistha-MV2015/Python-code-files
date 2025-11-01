'''Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.
'''
medical = input('Do you have any medical conditions ? Y for yes and N for no: ')
if medical == 'Y':
    print('you are eligible to take the exam.')
else:
    attend = int (input('Write your attendance percentage: '))
if attend > 75:
    print('you are eligible to take the exam.') 
else:
    print('You are not eligible to take the exam.')