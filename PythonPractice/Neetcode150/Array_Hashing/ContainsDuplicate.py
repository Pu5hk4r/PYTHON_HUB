def hasDuplicate(nums: list[int]) -> bool:
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False


def testcases():
    T = int(input("Enter number of test cases: "))

    while T > 0:
        print("Enter size and elements for the list")
        N = int(input("Size: "))
        l = []  # Initialize empty list
        print(f"Enter {N} integers:")
        # Input N integers
        l = list(map(int, input().split()))[:N]  # Take N integers from input

        # Check for duplicates and print result
        result = hasDuplicate(l)
        print("Contains duplicates:", result)

        T -= 1  # Decrement test case counter


# Run the test cases
if __name__ == "__main__":
    testcases()