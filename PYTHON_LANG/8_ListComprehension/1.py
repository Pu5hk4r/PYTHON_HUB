
# number = [1,2,3]
# new_number = [n+1 for n in number]
# name = "Pushkar"
# letter_list = [letter for letter in name]
# range_list = [num * 2 for num in range(1,5)]
# names = ["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
# short_names = [name for name in names if len(name) < 5]


l = [x for x in range(1, 5)]
print(l)

print()

m = [x**2 for x in range(1, 12)]
print(m)

print()

n = [x for x in 'ab*cdte' if x.isalpha()]
print(n)

print()

z = [x.lower() for x in 'PyThoN']
print(z)

print()

w = [int(x) for x in '12345']
print(w)

print()