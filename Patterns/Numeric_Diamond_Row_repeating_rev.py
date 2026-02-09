N = int(input("Enter Number"))
p = 1
for i in range(N-1):
    for j in range(i,N):
        print(' ',end= ' ')
    for j in range(i):
        print(p , end= ' ')
    for j in range(i + 1):
        print(p , end= ' ')
    p+=1
    print()

for i in range(N):
    for j in range(i + 1):
        print(' ',end= ' ')
    for j in range(i , N -1):
        print(p , end= ' ')
    for j in range(i , N):
        print(p , end= ' ')
    p-=1
    print()

