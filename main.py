def linear_Search(list1, n, key):

    for i in range(0, n):
        if (list1[i] == key):
            return i
    return -1


list1 = [4,7,88,45,153,65,85]
key = 7

n = len(list1)
res = linear_Search(list1, n, key)
if (res == -1):
    print("Element not found")
else:
    print("Element found at index: ", res)