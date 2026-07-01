# Q1
# row = 3
# col = 3
# x = [0] * row
# for i in range(row):
#     x[i] = [0] * col
#     for j in range(col):
#         x[i][j] = int(input("enter number"))
# print(x)
#
#
# def search(array, value):
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if value == array[i][j]:
#                 return f"the value in {i} {j}"
#     return "not in array"
#
#
# print(search(x, 0))
# Q 2
# def counter(array, value):
#     count = 0
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if value == array[i][j]:
#                count += 1
#     return count
# print(counter(x,2))

# Q3
# r =[[3, 1, 6], [2, 5, 0], [9, 7, 4]]
#
#
# def sort(array):
#     ineer = -1
#     outer = 0
#     ran = (len(array) * len(array[0]))
#     x = []
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             x.append(array[i][j])
#     x.sort()
#     num = 0
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#
#             array[i][j] = x[num]
#             num += 1
#
#     print(array)
#
# sort(r)

# Q4
#
# def matrix(row, col):
#     pos = 0
#     nigt = 0
#     zero = 0
#     array = [[0] * col] * row
#     for i in range(row):
#         for j in range(col):
#             n = int(input("enter number"))
#             if n > 0:
#                 pos += 1
#             elif n < 0 :
#                 nigt += 1
#             else:
#                 zero += 1
#             array[i][j] = n
#     print(array)
#     print(f"the positve = {pos}\nthe nigtive = {nigt}\nzeros = {zero}")
#
#matrix(3, 3)

# q 5
#
# x = [[1,2,3],
#      [2,1,3],
#      [2,3,1]]
# qut = 0
# up = 0
# down = 0
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         if i == j :
#             qut += x[i][j]
#         elif j> i:
#             up += x[i][j]
#         else:
#             down+= x[i][j]
# print(f"the qut = {qut}\ndown = {down}\nup = {up}")
#



