# question 1
# def count_words(text):
#     text = text.split()
#     print(len(text))
#
# count_words("hello world i am is fine")


# question 2

# x = "hi lora. \nhow are you?."
# def Count_none(text):
#     num = 0
#     for i in x:
#         if i.isspace():
#             continue
#         else:
#             num += 1
#     print(num)
# Count_none(x)


# Question 3

# def print_word_count(text):
#     text = text.split()
#     temp = []
#     for i in text:
#         if i not in temp:
#             print(f"{i} = [{text.count(i)}]")
#             temp.append(i)
#
# print_word_count("i am happy. i am a doctor. i like chocolate.")

# Question 4

# def proo(text1, text2):
#     text1 = text1.split()
#     text2 = text2.split()
#     if text2[0] != text1[0]:
#         print(f"text 1 id not start with {text2[0]} ")
#     else:
#         print(f"text 1 is start with {text2[0]} ")
#
# proo("hello world good mor","shello")



# Question 5

# def gogo(text1,text2):
#     if text1.endswith(text2):
#         print(True)
#     else:
#         print(False)
#
# gogo("hello world man"," man")   