def monotonic_array(array) -> bool:
    if len(array) <= 1:
        return True

    first = array[0]
    second = array[-1]  #array(len(array)-1)

    if first == second:
        for i in range(len(array) - 1):
            if array[i + 1] != array[i]:
                return False

    elif first < second:
        for i in range(len(array) - 1):
            if array[i + 1] < array[i]:
                return False

    else:
        for i in range(len(array) - 1):
            if array[i + 1] > array[i]:
                return False

    return True


# ✅ Test Cases
print(monotonic_array([]))                        # True
print(monotonic_array([5]))                       # True
print(monotonic_array([12, 245, 12, 23]))         # False
print(monotonic_array([-90, -12, -1, 12, 14, 24]))# True
print(monotonic_array([1, 2, 3, 4, 4]))           # True
print(monotonic_array([2, 2, 2, 2]))              # True
