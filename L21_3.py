M = [1, 2, 3, 4, 5, 6, 7, 8]
print("Original List :", M)

count = 0

for i in M:
    count += i

avg = count / len(M)

print("sum = ", count)
print("average = ", avg)

M.sort()

print("Smallest element is:", M[0])
print("Largest element is:", M[-1])
