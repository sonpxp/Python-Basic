# list_1 = ['The', 'Big', 'Bang', 'Theory']
# for key, value in enumerate(list_1):
#     print(key, value)

##########################

# list_2 = ['Geeks', 'for', 'Geeks', 'is', 'the', 'Best', 'Coding', 'Platform']
# for key, value in enumerate(list_2):
#     print(value, end=' ')

##########################
# zip

"""
Sử dụng zip ():  zip () được sử dụng để kết hợp 2 vùng chứa giống nhau
(list-list hoặc dict-dict) in các giá trị tuần tự.
Vòng lặp chỉ tồn tại cho đến khi vùng chứa nhỏ hơn kết thúc
"""

# # initializing list
# questions = ['name', 'colour', 'shape']
# answers = ['apple', 'red', 'a circle']
#
# # using zip() to combine two containers
# # and print values
# for question, answer in zip(questions, answers):
#     print(f'What is your {question}? I am {answer}.')

##########################
# ex1:
# d = {"geeks": "for", "only": "geeks"}
#
# # using items to print the dictionary key-value pair
# print("The key value pair using items is : ")
# for i, j in d.items():
#     print(i, j)
#
# # ex2:
# king = {'Akbar': 'The Great', 'Chandragupta': 'The Maurya',
#         'Modi': 'The Changer'}
#
# # using items to print the dictionary key-value pair
# for key, value in king.items():
#     print(key, value)

##########################

'''
Sử dụng sorted (): sorted () được sử dụng để in vùng chứa được sắp xếp thứ tự . 
Nó không sắp xếp vùng chứa mà chỉ in vùng chứa theo thứ tự đã sắp xếp cho 1 trường hợp. 
Việc sử dụng set () có thể được kết hợp để loại bỏ các lần xuất hiện trùng lặp .
'''

# python code to demonstrate working of sorted()

# initializing list
# lis = [1, 3, 5, 6, 2, 1, 3]
#
# # using sorted() to print the list in sorted order
# print("The list in sorted order is : ")
# for i in sorted(lis):
#     print(i, end=" ")
#
# print("\r")

# using sorted() and set() to print the list in sorted order
# use of set() removes duplicates.
# print("The list in sorted order (without duplicates) is : ")
# for i in sorted(set(lis)):
#     print(i, end=" ")
#
# print("\r")

# ex2:
# initializing list
# basket = ['guave', 'orange', 'apple', 'pear',
#           'guava', 'banana', 'grape']
#
# # using sorted() and set() to print the list
# #  in sorted order
# for fruit in sorted(set(basket)):
#     print(fruit)

##########################

# '''
# Using reversed(): reversed() is used to print the values of the container in the reversed order.
# It does not reflect any changes to the original list
# '''
#
# lis = [1, 3, 5, 6, 2, 1, 3]
#
# # using revered() to print the list in reversed order
# print("The list in reversed order is : ")
# for i in reversed(lis):
#     print(i, end=" ")

# using reversed() to print in reverse order
for i in reversed(range(1, 10, 3)):  # range(start, end, step)
    print(i)

##########################
