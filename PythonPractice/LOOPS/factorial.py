
num = int(input("Enter the Number"))

fact =  1

for i in range(1,num+1):

    if(num == 0):
        print("1")
        break

    fact = fact * i

print("Factorial", fact)
