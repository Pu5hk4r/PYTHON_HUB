n = 25
i = 1

while i <= 10:
    print(f"{n} X {i} = {n * i}")
    i += 1


print("---------------")

n = 4365

while n > 0:
    r = n % 10
    print(r)
    n = n // 10


# To get digit of a number
#
# n = 2546
#
# 2546 % 10 = 6
#
# r = n % 10

# To reduce a number
#
# n  = 2546
# 2546 // 10 = 254
#
# n = n // 10
