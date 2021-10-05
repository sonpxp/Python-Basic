'''
Random password generator
'''

import string
import random

LETTERS = string.ascii_letters  # -> lay ra cac chuoi a -> z
NUMBER = string.digits  # lay ra 0 -> 9
PUNCTUATION = string.punctuation  # _ / ...


# print(LETTERS, NUMBER, PUNCTUATION)


def password_generator(length=8):
    printable = f'{LETTERS}{NUMBER}{PUNCTUATION}'

    printable = list(printable)  # chuyen doi xang list de su dung random
    random.shuffle(printable)

    random_pass = random.choices(printable, k=length)
    random_pass = ''.join(random_pass)  # gan lai list -> chuoi string

    return random_pass


def get_password_length():
    pass_length = input("How long do you want your password: ")
    return int(pass_length)  # convert string -> int


def main():
    pass_length = get_password_length()
    password = password_generator(pass_length)

    print(password)


if __name__ == '__main__':
    main()
