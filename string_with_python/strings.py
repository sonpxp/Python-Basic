'''
Topic #2: Strings (chuoi ky tu) - a sequence of characters
'''

# String: ordered = theo thu tu, tuan tu
# String: immutable = khong the thay doi
# String: text presentation

# data type mutable: list, dict, set, bytearray
# data type immutable: int, float, decimal, complex, bool, bytes, string, tuple, range, frozenset

# using singe or double quotes
# my_string = "hello world"

'''
# Escaping Backslash (ctrl+ \)
'''
# my_string = 'I\'m a "Son"'
# print(my_string)

# char = my_string[1]
# print(char)

'''
# string is immutable --> cannot be changed
'''
# my_string = "hello world"
# my_string[0] = "M"  # khong the thay doi H -> M
# print(my_string)  # loi ko in ra duoc

'''
# substring with slicing
'''
# stringName[startIndex:endIndex]
# start at index 1 and go until index 5 (not include #5)
# my_string = "hello world"
# sub_string = my_string[1:5] # ello
# sub_string = my_string[:5] # hello
# sub_string = my_string[6:] # world
# sub_string = my_string[::2] # take every second character
# sub_string = my_string[::-1] # Reserse the string (dao nguoc chuoi)
# print(sub_string)

'''
# concatenate two or more strings 
# ket noi 2 hay nhieu chuoi lai voi nhau
# concat strings with +
'''

# getting = "Hello, Xin Chao Cac Ban"
# channel = "Dien May Xanh"
# sentence = getting + " Da den voi " + channel
# print(sentence)

# join elements of a list into a string: .join()
# my_list = ['how', 'old', 'are', 'your']
# sentence = '_'.join(my_list)
# print(sentence)


'''
# Iterating
'''
# Iterating over a string by using a for in loop
# my_string = "Hello, Xin Chao Cac Ban"
# for char in my_string:
#     print(char)

# check 1 ky tu co trong chuoi khong
# if "X" in my_string:
#     print("Yes")
# else:
#     print("No X")

'''
# Basic & Function  (ham co ban & huu ich)
'''
### strip()
# 'I am Alone' --> strips all whitespace characters form both ends

# print("    Alan Walker    ".strip())
# print("Ooh Nobita love Xuka".strip('0'))

### split() --> tach chuoi thanh 1 mang
# print('Ooh Nobita love Xuka'.split())  # --> ['Ooh', 'Nobita', 'love', 'Xuka']
# print('Ooh, Nobita, love Xuka'.split(','))  # --> ['Ooh', ' Nobita', ' love Xuka']


### replace() -> (str_old, new_str)
# print('Help me'.replace("me", "you"))

## startswith(bat dau) - endswith(ket thuc)
# my_string = "And cook rice"
# print(my_string.startswith("And"))  # True or False -> True
# print(my_string.endswith("rices"))  # True or False -> False

## index and find -> get position string
# my_string = "Bye bye"
# print(my_string.index('e'))
# print(my_string.find('e'))

## TextStyle
# my_string = "xin chao"
# print(my_string.upper()) # -> XIN CHAO

# my_string = "ANH EM"
# print(my_string.lower())  # -> anh em
#
# my_string = "how are you?"
# print(my_string.title())  # -> How Are You?
#
# my_string = "ok, i am fine thank you"
# print(my_string.capitalize())  # -> Ok, i am fine thank you
# print(my_string.count('a'))  # -> 2 chu a


'''
# String formatting
# %, .format(), f-Strings (new version python 3.6 ->>)
'''

## %
# name = "FPT"
# my_string = "Welcome to %s" % name
# print(my_string)

# pi = 3.14159  # float
# s = "pi number"
# my_string = "Variable is %f" % pi # -> ghep string
# my_string = "Variable is %f %s" %(pi, s) # -> ghep string + float
# my_string = "Variable is %.2f %s" % (pi, s)  # -> lay 2 chu so thap phan
# print(my_string)

## .format()

# age = 24
# height = 180.5
# my_string = "I am {} year old, {:.2f} cm".format(age, height)
# print(my_string)


## f-Strings (ver: python 3.6 >>)
pi = 3.14159  # float
name = "Join"
age = "24"
my_string = f"Pi is {pi:.2f} and my name is {name}; age {age} years old"
print(my_string)