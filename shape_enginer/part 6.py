# حل التمرين الاول
# n = 9
# half = (n//2)+1
# k = 2
# for i in range(1,n+1):
#     if i < half:
#         print('*'*i, f' '*(n-(i*2)), '*'*i)
#     elif i == half:
#         print('*'*(n+1))
#     else:
#         print(f'*'*(i-k), f'{((i*2)-((half*2)+1))}'*((i*2)-((half*2)+1)), '*'*(i-k))
#         k += 2

# الحل باللنستد لوب

# n = 9
# half = (n//2)+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i <= half:
#             if j <= i or j>(n-i):
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#         else:
#             if j >= i or j<=((n+1)-i):
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#     print()

# حل التمرين الثاني
# n = 9
# half = (n // 2) + 1
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i <= half:
#             if i <= j < (n - (i - 2)):
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
#         else:
#             if j <= i and j >= (((n + 1) - i)):
#                 print('*', end=f' ')
#             else:
#                 print(' ', end=' ')
#     print()

# التمرين الثاني بضرب النجوم

# n = 11
# space = 0
# for i in range(0,n+1):
#     if i <= (n//2):
#         print(f' '*i,'*'*(n-space))
#         space += 2
#         continue
#     elif space > n:
#         space -= 2
#     else:
#         space -= 2
#         print(f' '* (space//2),end=' ')
#         print(f'*'*(n-space))


# حل التمرين الثالث
# n = 9
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i < (n // 2) + 1:
#             if j <= i or j > (n - i):  # or (j >= i or j <= (n-i)):
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
#         elif i > (n // 2) + 1:
#             if j >= i or j <= (n - (i - 1)):
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
#     print()
# -------------------->
# حل بطريقه الشرط الطويل
# <----------------------
# n = 9
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if ((n//2)+1 > i and(j <= i or j > (n - i))) or (((n//2)+1 < i)and (j >= i or j <= (n - (i - 1)))):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# ------------------->
# حل التمرين الرابع
# < -----------------
# بالضرب
# n = 9
# half = n//2
# star =1
# for i in range(0,n):
#     if i < half :
#         print(' '*i,'*'*(half-i),' '*2,'*'*(half-i))
#     elif i > half:
#         print(f' '*((n-i)-1),'*'*star,' '*2,'*'*star)
#         star+=1

# n = 9
# half = (n//2)+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i < half :
#             if i <= j < half or j > (n+i) - (half) :
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#     print( )
# حل التمرين الخمامس بالضرب
# n = 9
# half = (n//2)+1
# for i in range(1,n+1):
#     if i < half:
#         print('*'*((n-1)//2),' ','*'*((n-1)//2))
#     elif i > half:
#         print('*' * ((n - 1) // 2), ' ' , '*' * ((n - 1) // 2))
#
#     else:
#         print( )

# حل باللوب المتداخله

# n = 9
# half = (n//2)+1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#
#         if i < half:
#             if j > half or j < half:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#         elif i > half:
#             if j > half or j < half:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#     print()


# if j >= i or j <= ((n + 1) - i):
#     print('*', end=' ')
# else:
#     print(' ', end=' ')
