

def count_Number(number):

    count = 0

    while(number > 0):

        number  = number // 10
        count = count +1

    return count

def sumofdigit(number):

    sum = 0

    while(number > 0):
        r = number % 10 
        number  = number // 10   
        sum += r

    return sum


def reverseNumber(number):

    rev = 0

    while number > 0 :

        r = number % 10

        number = number // 10

        rev = rev * 10 + r

    
    return rev


def palindrome(number):

    rev = 0

    while number > 0 :

        r = number % 10

        number = number // 10

        rev = rev * 10 + r

    
    return rev


    



num = int(input("Enter the number"))

digit = count_Number(num)

summ = sumofdigit(num)

ulta = reverseNumber(num)

print(f"number of digit present in {num} is {digit}\n")
print(f"sum of digit is {summ}\n")
print(f"Reverse : {ulta}")
