#W4
#4.1
#1
import math
n = math.pi
vector = [n, n, n]
print(vector)
print([n]*3)
#2
matrix =[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0])
print(matrix[1])
print(matrix[2])



matrix[1][1] = 99
print("Matrix wurde gändert")
for row in matrix:
    print(row)

#4.2
list_ = [["Jacob", 24, 1.84], ["Lisa", 23, 1.75], ["Alex", 20, 1.70]]
list_.sort()
print(list_)
for row in list_:
    print(row)