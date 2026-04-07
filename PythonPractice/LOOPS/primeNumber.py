num = int(input("Enter the number: "))

if num < 2:
    print("Not a Prime Number")
else:
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print("Prime number")
    else:
        print("Not a Prime Number")
