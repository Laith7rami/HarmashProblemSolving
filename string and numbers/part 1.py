# soul 1
# n = '123'
# total = 0
# for i in n:
#     total += int(i)
# print(total)

'''

إذا كنت تتعامل مع عدد صحيح إسمه n و قلت n % 10 فأنت بذلك ستحصل على أخر عدد موجود في الرقم.
و إذا قلت n / 10 فأنت بذلك ستتخلص من أخر عدد كان موجوداً في الرقم.


الحل بلغة بايثون
s = 0
n = int(input('Enter a number: '))
while n != 0:
    s += n % 10
    n = int(n / 10)
print('The sum of the digits is: ' + str(s))

'''


# soul 2
# n = '54321'
# print(n[::-1])
#
# n = '54321'
# for i in range(len(n)-1,-1,-1):
#     print(int(n[i]),end='')

# soul 3
# n = '123210'
# if n == n[::-1]:
#     print('it is palindrome')
# else:
#     print('it is not  palindrome')
# test = ''
# for i in range(len(n)-1,-1,-1):
#      test += n[i]
# if n == n[::-1]:
#     print('it is palindrome')
# else:
#     print('it is not  palindrome')
#
# sou; 4
#
# def count(first_text=input("enter first"), seconde_text=input("enter sec")):
#     #print(first_text.count(seconde_text))
#     first_text = first_text.split()
#
# count()

# soul 5
#
# def stre(text=input('enter')):
#     # for i in range(len(text)-1,-1,-1):
#     #     print(text[i],end='')
#     print(text[::-1])
# stre()