def contain_duplicate_set(nums): #TC O(N'2)
    unique = set()

    for i in nums:
        if i in unique:
            return True
        unique.add(i)
    return False


def contain_duplicate_Sort(nums): #TC O(n log n)
    nums.sort() #in-place sort-modifies input

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return  False

def contains_duplicate_BruteForce(nums): #TC O(n)
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                return True
        return False


