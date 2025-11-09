word = input('please enter the word: ')
charecter = input('please enter the charecter you want to search: ')

c = 0
s = 0
while s < len(word):
    if word [s] == charecter:
        c = c+1
    s = s+1
print('The word' , word , ' has a number of ' , c , ' charecters of ' , charecter)