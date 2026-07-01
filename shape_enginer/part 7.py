# حل التمرين الاول
# الحل باللوب
# n = 11
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j == 1 or j == i or j == n or j == (n - (i - 1)):
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# حل التمرين الثاني
# n = 11
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i ==1 or i ==n or j ==i or j == n-(i-1):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print( )


# حل التمرين الثالث

# n = 11
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if (((j == 1 or j == i) or j == n or j == (n - (i - 1))) and j != (n // 2) + 1) or (
#                 (i == (n // 2) or i == (n // 2) + 1) and (j != ((n // 2) + 1))):
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

#  حل التمرين الرابع
# n = 11
# half = n //2
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if (((i == 1 or i==n) and j != half+1) or (j == half or j == half+2) or j == (n - (i - 1)) or (j == i)) and i != half+1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print( )

# حل التمرين الخامس
# n = 11
# half = n // 2
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if ((i == 1 or i == n or i == (n // 2) or i == (n // 2) + 2) and j != (n // 2) + 1) or (
#                 j == 1 or j == n or j == (n // 2) or j == (n // 2) + 2 and j != (n // 2) + 1) and i != (n // 2) + 1 :
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
