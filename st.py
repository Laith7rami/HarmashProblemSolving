# التمرين الثالث من الجزء الثاني
# rows = int(input('rows'))
# x = rows//2
# for i in range(1,rows,1):
#     if i <= x:
#
#         print('  '*(x - i),'* '* i )
#     else:
#         print('  '*(i-x),'* '* (x - (i-x)) )

# التمرين الاول من الجزء الثالث
# star = 11
# x = star // 2
# space = 1
# for i in range(1, star * 2, 2):
#     if i > star:
#         star -= 2
#         print('  ' * space, ' *' * star, )
#         space += 1
#
#         continue
#
#     print(f'  ' * x, ' *' * i, )
#     x -= 1




# حل التمرين الثاني من الجزء الثالث
# star = 9
# x = star // 2
# space = 1
# space_in = 1
# print('  ' * x, '  *' * 1, )
# for i in range(1, star*2 , 2):
#     if i > star:
#         if space_in > star:
#             space_in -= 2
#
#         space_in -= 2
#         print('  ' * space , '*' ,'  '*space_in, '*')
#         space += 1
#
#         continue
#
#     print('  ' * x, '*' ,'  '*space_in, '*')
#     x -= 1
#     space_in += 2
# print('  ' *( (star//2) +1), '*' * 1, )
# -.... حل التمرين الثالث من الجزء الثالث
# star = 9
# x = star // 2
# space = 1
# space_in = 1
# print('- ' * x, ' *' * 1, )
# for i in range(1, star*2 , 2):
#     if i > star:
#         if space_in > star:
#             space_in -= 2
#
#         space_in -= 2
#         print('- ' * space , '*' ,'  '*space_in, '*')
#         space += 1
#
#         continue
#
#     print('- ' * x, '*' ,'  '*space_in, '*')
#     x -= 1
#     space_in += 2
# print('- ' *( (star//2) +1), '*' * 1, )

# حل التمرين الرابع من الجزء الثالث
# n = 10
# for i in range(1,n+1):
#     if i == 1 or i == n:
#         print('*',' * ' * (n-2),'*')
#     else:
#         print('*','   ' * (n-2),'*')

# حل التمرين الخامس من الجزء الثالث
# n = 7
# for i in range(1,n+1):
#     if i == 1 or i == n:
#         print('*',' * ' * (n*2),'*')
#     else:
#         print('*','   ' * (n*2),'*')

#  حل التمرين الاول من الجزء الرابع
# n = 10
# for i in range(0,n):
#     print('* '*i,' *'*((n-1)-i))
