def binarysearch(sorted_num, key):
    left = 0
    right = len(sorted_num) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if sorted_num[mid] == key:
            return mid
        elif sorted_num[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Sort beforehand
lst = [-12, 45, 12, 10, 89, 100, 0, 23, -24]
sorted_lst = sorted(lst) #sorted is iterable list, tuple ,return  set,new sorted list and original stays unchanged
key = 0                  # sort() list only nothing return inplace sorting

index = binarysearch(sorted_lst, key)
if index != -1:
    print(f"Found at index {index} in sorted list: {sorted_lst}")
else:
    print("Not found!")



# def binarysearch(num, key):
#     num.sort()  # OK here since we don't care about original index
#     left = 0
#     right = len(num) - 1
#
#     while left <= right:
#         mid = left + (right - left) // 2
#
#         if num[mid] == key:
#             return True
#         elif num[mid] < key:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return False
#
# lst = [-12, 45, 12, 10, 89, 100, 0, 23, -24]
#
# if binarysearch(lst, 0):
#     print("Found!")
# else:
#     print("Not found!")
