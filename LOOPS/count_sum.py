# number  = int(input("enter the number"))
#
# sum = 0
#
# i = 0
#
# while number > 0:
#
#     r = number % 10
#
#     number = number // 10
#
#     sum += r
#
#     i +=1
#
# print(f"Sum of digits {number} is : {sum}")
# print(f"count of digit is : {i}")
#

def sum_count(number):
    sum = 0
    count = 0

    while number > 0:
        r = number % 10
        number = number // 10

        sum += r
        count += 1

    print('Sum',sum)
    print('\nCount', count)


numb = int(input("enter the number"))
sum_count(numb)


