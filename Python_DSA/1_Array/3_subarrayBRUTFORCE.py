
#BRUTFORCE O(N'3)

def subarray_sum(arr):

    largest_sum = 0

    n = len(arr)

    for i in range(n):
        for j in range(i+1, n+1):
            subarray_sum = 0

            for k in range(i,j):

                subarray_sum += arr[k]

            largest_sum = max(largest_sum,subarray_sum)

    return  largest_sum

if __name__ == "__main__":
    arr = [10, 15, 12, 9, 6, 4, 3, 10, 8]

    sum_result = subarray_sum(arr)
    if sum_result != -1:
        print("The sum using brute force is:", sum_result)
    else:
        print("Sum is NOT Found!")