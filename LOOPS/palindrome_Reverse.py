def palindrome(number):

    original = number

    rev = 0

    while number > 0:

        r = number % 10
        number = number // 10

        rev = rev * 10 + r


    if original == rev:
        print(f"Yes! {original} is Palindrome Number")
    else:
        print(f"Noah! {original} is Palindrome Number")


    print(f"\nReverse of {original} is {rev} ")


num = int(input("Enter the number"))
palindrome(num)

