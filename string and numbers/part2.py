# soul1
# def remove(one, tow):

# fisrt method
# new_text = ''
# one = one.split()
# for i in one:
#     if tow in i:
#         new_text += ''
#     else:
#         new_text+= f'{i} '
# print(new_text)

# seconde method

# new_text = ''
# start = 0
# for i in range(one.count(tow)):
#     new_text += one[start:one.index(tow, start)]
#     start = one.index(tow, start) + len(tow)
#
# new_text += one[start:]
#
# print(new_text)

# remove('hello cat how are you cats i am cs', 'cat')

# soul 2
# def relace(one,tow,word):
# first method
# new_text = ''
# start = 0
# for i in range(one.count(tow)):
#     new_text += one[start:one.index(tow, start)] + word
#     start = one.index(tow, start) + len(tow)
#
# new_text += one[start:]
#
# print(new_text)
# seconde method

#     one = one.split()
#     new = ''
#     for i in one:
#         if tow not in i:
#             new += f'{i} '
#         else:
#             new += f'{word} '
#     print(new)
# relace('hello cat how are you cats i am cs', 'cat','dog')


# soul 3
# def duoble(text):
#     new = ''
#     for i in text:
#         if i != ' ':
#             new += f'{i*2}'
#         else:
#             new += i
#     print(new)
# duoble('iron Man')


# soul 4


# soul 5
#
# def index(text, word):
#
#     #text = text.split()
#     for i in range(0,len(text)):
#         if text[i] == word:
#             print(i)
#
# index("Harmash is the best site to learn programming",'a'
# )
#
#
