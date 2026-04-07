num = int(input("Enter the number"))

count = 0
max = float('-inf') #for positive only value initialise with 0 only
min = float('inf')

print(f"plz enter {num} numbers:")

while count < num:
    count += 1
    n = int(input(""))

    if(n > max):
        max = n
    if(min > n):
        min = n


print("Max Element" , max)
print("Min Element", min)
