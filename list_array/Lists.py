"""
Topic #7: List trong Python - một dạng dữ liệu cho phép lưu trữ nhiều kiểu dữ liệu khác nhau trong nó,
và chũng ta có thể truy xuất đến các phần tử bên trong nó thông qua vị trí(index) của phần tử đó trong list
Ngôn Ngữ Khác: C/C++, Java, List trong Python = Mảng (Array)
"""

'''
1. creating a list
'''

list_1 = ['banana', 'apple', 'orange', 'cherry', 'caffe']
list_2 = ['banana', 23, True, None]
list_3 = list()  # empty list

# print(list_2)

'''
2. Access elements: Truy cập đến các giá trị trong list
'''

my_list = [1, 2, 3, 3, '3', '3', 3, '4', True]

# print(len(my_list))  # in ra do dai list
# print(my_list[2])  # in ra phan tu thu 2
# print(my_list.count(3))  # in ra so luong phan tu giong nhau
# print(my_list.index(3))  # in ra vi tri phan tu muon biet

# for item in my_list:
#     print(item)

# Python’s built-in enumerate function
# allows us to loop over a list and retrieve
# both the index and the value of each item in the list
presidents = ["Washington", "Adams", "Jefferson",
              "Madison", "Monroe", "Adams", "Jackson"]

# for index, name in enumerate(presidents, start=1):
#     print(f"President {index}: {name}")

# Slicing
# : is called slicing and
# has the format [ start : end : step ]
# my_list[3]  # True
# my_list[1:]  # [2, '3', True]
# my_list[:1]  # [1]
# my_list[-1]  # True
# my_list[::1]  # [1, 2, '3', True]
# # Reverse List by Slicing
# my_list[::-1]  # [True, '3', 2, 1]
# my_list[0:3:2]  # [1, '3']

print("Hello world")
print("Hello world2")
print("Hello world3")