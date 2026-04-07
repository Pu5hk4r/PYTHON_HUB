

students_heights = [141,156,187,171,178,165]

for n in range(0,len(students_heights)):
    students_heights[n] = int(students_heights[n])


total_height =0

for height in students_heights:
    total_height += height
print(f"total height = {total_height}")

number_of_students =0

for student in students_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")