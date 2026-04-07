# KADANE's Algorithm (Iterative)
def max_subarray(nums):
    if not nums:  # Corrected the condition to check if the array is empty
        return 0

    current_sum = nums[0]
    largest_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])  # Update current_sum
        largest_sum = max(largest_sum, current_sum)  # Update largest_sum

    return largest_sum


if __name__ == "__main__":
    arr = [10, -15, 12, -9, 6, -4, 3, 10, -8]

    sum_result = max_subarray(arr)
    if sum_result != -1:  # Kadane's algorithm doesn't return -1; this condition is unnecessary
        print("The sum of the maximum subarray is:", sum_result)
    else:
        print("Sum is NOT Found!")
