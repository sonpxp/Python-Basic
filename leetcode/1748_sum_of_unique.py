# def sumOfUnique(nums: []):
#     s = set(nums)
#     for i in nums:
#         if nums.count(i) > 1 and i in s:
#             s.remove(i)
#     return sum(s)
import collections


def sumOfUnique1(nums: [int]) -> int:
    hashmap = {}
    sum = 0

    for i in nums:
        if i in hashmap.keys():
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    for k, v in hashmap.items():
        print(k, v)
        if v == 1:
            sum += k
    return sum


def sumOfUnique2(nums: [int]):
    lis = []
    for a, c in collections.Counter(nums).items():
        if c == 1:
            lis.append(a)
    return sum(lis)
    # one line
    # return sum(a for a, c in collections.Counter(nums).items() if c == 1)


################################

nums = [2, 2, 3, 4, 5, 5, 5, 6]

# print(sumOfUnique(nums))
# print(sumOfUnique1(nums))
print(sumOfUnique2(nums))


