students_scores = [41,56,87,71,78,65,91,96]

for n in range(0,len(students_scores)):
    students_scores[n] = int(students_scores[n])

highest_score = 0

for score in students_scores:
    if score > highest_score:
        highest_score = score


print(f"The highest score is in the class is : {highest_score}")