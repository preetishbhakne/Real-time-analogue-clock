def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if list1[mid] < n:
            low = mid + 1

            # If n is greater, compare to the right of mid
        elif list1[mid] > n:
            high = mid - 1


        else:
            return mid


    return -1

list1 = [13,26,39,45,54,7]
n = 45
result = binary_search(list1, n)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list1")