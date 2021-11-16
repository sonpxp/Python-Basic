from collections import Counter


def kthDistinct(arr: [str], k: int) -> str:
    arr = [i for i in arr if arr.count(i) == 1]
    print(arr)
    return "" if k > len(arr) else arr[k - 1]


def kthDistinct1(arr: [str], k: int) -> str:
    res = Counter(arr)

    for x in arr:
        if res[x] == 1:
            k -= 1
        if k == 0:
            return x
    return ""


def kthDistinct2(arr: [str], k: int) -> str:
    dict = {}
    for key in arr:
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    count = 0
    for key in dict:
        if dict[key] == 1:
            count += 1
            if count == k:
                return key
    return ""


########################
arr = ["d", "b", "c", "b", "c", "a", "m", "n"]
k = 3
print(kthDistinct(arr, k))
