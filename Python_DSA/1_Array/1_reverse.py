def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end :
        arr[start] , arr[end] = arr[end], arr[start]

        start += 1
        end -= 1

if __name__ == "__main__":
    arr = [10, 20, 30, 45, 60, 80, 90]

    # Print the output
    print("Original Array:", arr)

    reverse_array(arr)

    # Print the reversed output
    print("Reversed Array:", arr)