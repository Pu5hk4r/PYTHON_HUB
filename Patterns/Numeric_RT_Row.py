N = int(input("Enter Number"))

for i in range(N):
    p = 1
    for j in range(i+1):
        print(p , end= " ")
        p+=1
    print()