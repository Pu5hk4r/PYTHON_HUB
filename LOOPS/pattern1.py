num = int(input("Enter the Number: "))

space = num * 2  # space between triangles

for i in range(1, num + 1):
    # Left triangle
    for j in range(1, i + 1):
        print("*", end="")

    # Space in the middle
    for k in range(space - 2 * i):
        print(" ", end="")

    # Right triangle
    for p in range(1, i + 1):
        print("*", end="")

    print()  # Move to next line
