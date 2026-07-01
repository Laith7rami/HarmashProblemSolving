import  random
# Q1
# def print_seconde_mix(array):
#     mix = 0
#     seconde = 0
#     for i in range(len(array)):
#         if mix < array[i]: mix = array[i]
#     for i in range(len(array)):
#         if seconde < array[i] < mix: seconde = array[i]
#     print(mix , seconde)
#
# print_seconde_mix([1,6,3,8,1,0,4,9,90,12,35,7,30,18,20])

# # Q2
# def print_seconde_mix(array):
#     loews = array[0]
#     seconde = array[0]
#     for i in range(len(array)):
#
#         if loews > array[i]: loews = array[i]
#
#     for i in range(len(array)):
#         if seconde > array[i] > loews: seconde = array[i]
#     print(loews , seconde)
#
# print_seconde_mix([1,6,3,8,1,0,4,9,90,12,35,7,30,18,20,-12])
#

# # Q3
# def random_array(n):
#     array = [0]*n
#     for i in range(n):
#         array[i] = random.randint(1,10)
#     print(array)
# random_array(6)

# Q 4

# def long_name(array):
#     long_n = ''
#     for i in range(len(array)):
#         if len(array[i]) > len(long_n) : long_n = array[i]
#     print(long_n)
#
# long_name(["ahmed","salem","levi"])

# # Q5
# def compar_array(x,y):
#
#     for i in range(len(x)):
#         if x[i] == y[i]:
#             pass
#         else:
#             print('the arrays not equals')
#             return
#     print('the tow array is equals')
# compar_array([1,2,3],[1,0,3])