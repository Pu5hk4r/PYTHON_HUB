import math

def paint_cal(height,width,cover):

    nums_can = (height*width) /cover
    round_up_cans = math.ceil(nums_can)
    print(f"You will need {round_up_cans} cans of paint.")


h = int(input("Enter the height"))
w = int(input("Enter the width"))
coverage = 5
paint_cal(height=h,width=w,cover=coverage)