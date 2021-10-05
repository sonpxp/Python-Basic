# Basics data type


"""
cac kieu du lieu co ban: bool, None, int, float, str
"""

'''
top #0: bool, None
'''

# [x] bool: true & false
# var_bool = True

# print(type(var_bool))

# Numerically, they're evaluated as integers with value 1(True), 0 (False)
# a = 4 + True
# print(a)
# neu ket qua = 5 thi True = 1

# b = False
# if b == 0:
#     print("B = 0")

# [x] None: phan tu khong

# var_none = None
# print(type(var_none))

# None is often used as a placeholder for optional or missing value
# It evaluates as False in conditionals.

# email_address = None #False
# email_address = "xuanson@gmail.com"
#
# if email_address:
#     print(f"Email address is: {email_address}")
# else:
#     print(f"Email address is empty or: {email_address}")

'''
top #1: Number (int, float)
'''

# int
# print(type(1))
# print(type(0))
# print(type(-10))


# float
# print(type(0.0))
# print(type(2.340))
# print(type(3E2), 3E2) # 3*10(^2)

# [x] Arithmetic: cac phep toan: +, -, *, / , **, //, %
# print(10 + 5)  # 15
# print(10 - 5)  # 5
# print(10 * 5)  # 50
# print(10 / 3)  # 3.33333...
# print(10 // 3)  # 3
# print(10 % 3)  # 1 vi 10/3 = 3 du 1 (chia lay du)
# print(10 ** 3)  # 10^3 = 10*10*10 = 1000

# [x] Basic Function
print(pow(10, 3))  # 10^3 ~ 10 ** 3 = 1000
print(abs(-8.9))  # 8.9 (gia tri tuyet doi x)
print(round(8.86))  # 9 (lam tron)
print(round(8.8366846, 3) ) # 8.837 (lam tron den so thu 3) --> round to nth digit
print(bin(512)) #'0b1000000000' --> binary format
print(hex(521)) #'0x209' --> hexadecial format (thap luc phan)