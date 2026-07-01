# Q1

# num1 = int(input("enter num1 "))
# num2 = int(input("enter num2 "))
# if num2 > num1:
#     print(f"{num2} > {num1}")
# elif num1 == num2:
#     print(f"{num2} == {num1}")
# else:
#     print(f"{num2} < {num1}")

# Q2
# def compar(*args):
#     big = 0
#     for i in args:
#         if i > big:
#             big = i
#     print(big)
#
# compar(1,56,3,7,4,3,6,3,64,565)
#Q 3

# n = int(input("enter num"))
# s = 0
# print("s = ",end=' ')
# for i in range(1,n+1):
#     if i % 2 != 0:
#         print(f"-{i}",end=' ')
#     else:
#         print(f"+{i}",end=' ')