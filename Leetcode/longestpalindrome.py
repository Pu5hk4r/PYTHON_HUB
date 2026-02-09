def palindrome(s: str) -> int:
    count = [0] * 128
    ans = 0

    for char in s:  # Fix: iterate directly over characters, not index
        count[ord(char)] += 1

    for c in count:  # Fix: c is the value (frequency), not the index
        ans += (c // 2) * 2

    if ans < len(s):  # Fix: should be '<', not '<='
        ans += 1

    return ans


st = input("Enter the string: ")
print("Longest palindrome that can be built is:", palindrome(st))
