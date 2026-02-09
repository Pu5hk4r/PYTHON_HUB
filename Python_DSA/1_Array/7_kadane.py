def max_subarray_sum(arr):
    all_negative = all(x <= 0 for x in arr)
    if all_negative:
        return max(arr)

    current_sum = 0
    max_sum = float('-inf')

    for x in arr:
        current_sum += x
        if current_sum < 0:
            current_sum = 0
        max_sum  = max(max_sum , current_sum)
    return  max_sum

vec = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_subarray_sum(vec))