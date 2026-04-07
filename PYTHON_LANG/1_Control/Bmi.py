

height = float(input("Enter the height in metre "))

weight = int(input("Enter the weight in metre "))

bmi = weight / (height*height)

if bmi <18.5:
    print(f"your BMI is {bmi}, you are underweight.")
elif bmi <25:
    print(f"your BMI is {bmi}, you are normal weight.")
elif bmi <30:
    print(f"your BMI is {bmi}, you are slightly overrweight.")
elif bmi<35:
    print(f"your BMI is {bmi}, you are obese.")
