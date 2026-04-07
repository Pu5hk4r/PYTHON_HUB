#T/C O(log N)
def lowerbound(num, val):
    low = 0
    high = len(num) - 1
    result = -1

    while low <= high:
        mid = low + (high - low)//2
        if num[mid] == val:
            return  val
        elif num[mid] < val:
            result = num[mid]
            low = mid + 1
        else:
            high = mid - 1

    return  result


def upperbound(num, val):
    low = 0
    high = len(num) - 1
    result = -1

    while low <= high:
        mid =  (low + high)// 2

        if num[mid] > val:
            result = num[mid]
            high = mid - 1
        else:
            low = mid + 1

    return result

arr = [1, 3, 5, 7, 9]
val = 5
print("UpperBound",upperbound(arr, val))
print("LowerBound",lowerbound(arr, val))