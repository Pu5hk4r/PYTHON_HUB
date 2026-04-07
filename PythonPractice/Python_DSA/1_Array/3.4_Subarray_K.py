#kadane algo with early reset

def max_subarray(nums):
    res = float('-inf') # initiliaze result to the smallest possible value
    cur = 0

    for num in nums:

        cur += num
        res =  max(res, cur)

        if cur < 0:
            cur = 0

    return res

if __name__ == "__main__":
    arr = [-10, -15, -12, -9, -6, -4, -3, -10, -8]

    sum_result = max_subarray(arr)
    if sum_result != -1:  # Kadane's algorithm doesn't return -1; this condition is unnecessary
        print("The sum of the maximum subarray is:", sum_result)
    else:
        print("Sum is NOT Found!")