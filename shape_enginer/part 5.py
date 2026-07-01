# حل التمرين الاول
# n = 9
# for i in range(1,n+1):
#     if i < ((n//2)+1):
#         print(f'  '*(n//2),'* '*((n//2)+1))
#     elif i == ((n//2)+1):
#         print('* '*n)
#     else:
#         print('* ' * ((n // 2) + 1),f' ' * (n // 2))

# حل تحر
# n = 9
# for i in range(1,n+1):
#     if i == (n // 2) + 1:
#         print('* ' * n)
#         continue
#     for j in range(1,n+1):
#         if i < (n//2)+1:
#             if j >= (n//2)+1:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#
#         else:
#             if j <= (n//2)+1:
#                 print('*',end=' ')
#             else:
#                 print(' ',end='')
#
#     print( )

# حل التمرين الثاني


# n = 9
# for i in range(1,n+1):
#     if i == (n // 2) + 1:
#         print('* ' * n)
#         continue
#     for j in range(1,n+1):
#         if i < (n//2)+1:
#             if j <= (n//2)+1:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#
#         else:
#             if j >= (n//2)+1:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#
#     print( )


# حل التمرين الثالث
# n = 11
# half = n // 2
# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print(f' ' * ((n - 2) - (i - 1)), '* ' * (half + 1))
#         continue
#
#     if i < half + 1:
#         print(' ' * (n - 2), '*', ' ' * (half + 1), '*')
#     elif i == half + 1:
#         print('* ' * n)
#     else:
#         print('*', ' ' * (half + 1), '*')



# حل التمرين الخماس
# n = 7
# for i in range(0,n):
#     print('0'*i,'*','1'*((n-1)-i))
