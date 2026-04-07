num = int(input("Enter the number"))

fib_0 = 0
fib_1 = 1

for i in range(0,num):
    fib = fib_0 + fib_1
    fib_0 = fib_1
    fib_1 = fib


print("Fibonacci", fib_0)