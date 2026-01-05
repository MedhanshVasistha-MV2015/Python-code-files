st = int(input("Enter the starting number: "))
end = 6

nl = []
for i in range(st, end + 1):
    nl.append(i)

print("Full list:", nl)

el = []
ol = []

for e in nl:
    if e % 2 == 0:
        el.append(e)
    else:
        ol.append(e)

print("Even numbers:", el)
print("Odd numbers:", ol)
