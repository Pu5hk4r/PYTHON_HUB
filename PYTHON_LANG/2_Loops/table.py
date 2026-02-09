

number = int(input("enter the number"))

count = 1


while(count):

    r = number*count

    print(f"{number} x {count} = {r}")

    count = count+1

    if(count > 10):

        break


