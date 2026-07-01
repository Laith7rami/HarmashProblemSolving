#  حل التمرين الاول من الجزء الرابع
# n = 10
# for i in range(0,n):
#     print('* '*i,' *'*((n-1)-i))

# التمرين الثاني

# n = 9 - 2
# for i in range(0,n+2,):
#     if i < 4:
#
#         print('* '*i,' *'*(n-(i*2)),' *'*i)
#     # elif i == 4:
#     #     print('* ' * i, ' *' * i)
#
#     else:
#         print('* '*((n-i)+1),' *'*(n-(((n-i)+1)*2)),' *'*((n-i)+1))

# حل التمرين الثالث
# n = 9
# for i in range(1,n+1,):
#     if i < 5:
#
#         print(f' '*i,'*'*1,f'{((n-2)-((i-1)*2))}'*((n-2)-((i-1)*2)),'*'*1)
#     elif i == 5:
#         print(f' ' * (i+1),'*')
#
#     else:
#         print(f' '*((n+1)-(i)),'*'*1,f'{((i*2)-(n+2))}'*((i*2)-(n+2)),'*'*1)


# حل التمرين الرابع
#n = 9 - 2

# for i in range(0, n + 1, ):
#
#     if i == 0:
#         print('* ' * (n))
#
#
#     elif i < (n // 2) + 1:
#         print('*', end='')
#
#         print(f' ' * (i - 1), '*' * 1, f'{((n - 2) - ((i - 1) * 2))}' * ((n - 2) - ((i - 1) * 2)), '*' * 1,
#               end=f' ' * (i))
#         print('*')
#     elif i == (n // 2) + 1:
#         print('*', end=' ')
#         print(f' ' * (i - 1), '*', end=f' ' *(i+1))
#         print('*')
#
#     else:
#         print('*', end='')
#         print(f' ' * ((n + 1) - (i + 1)), '*' * 1, f'{((i * 2) - (n + 2))}' * ((i * 2) - (n + 2)), '*' * 1,
#               end=f' ' *(i-(((i * 2) - (n + 2))+1)))
#         print('*')
# print('* ' * (n))

# حل التمرين الرابع بطريقه هرموش
# n = 0
# while n <= 0:
#     n = int(input("Enter the number of lines: "))
# if n % 2 == 0:
#     n += 1
# for i in range(1, n + 1):
#     if i == 1:
#         print('* '*(n-1))
#     print('*',end=' ')
#     for j in range(1, n + 1):
#         if i == j or j == n - i + 1 :
#             print('*', end=' ')
#         else:
#             print(' ', end='')
#     print('*')
# print('* '* (n-1))


#  حل التمرين الخامس مع الجزء الرابع
# n = 9
# sqr = int(n**0.5)+2
# for i in range(1,n+1):
#     if i == 1 or i == n or i == ((n//2)+1):
#         print('* '*(n))
#     else:
#         print('*',f' '*sqr,'*',' '*sqr,'*')

# حل اخر بالنستد لوب
# n = 11
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == ((n//2)+1) or i == n:
#             print('*',end=f' ')
#         elif j == 1 or j  == ((n//2)+1) or j == n:
#             print('*',end=f' ')
#         else:
#             print(' ',end=f' ')
#     print()



