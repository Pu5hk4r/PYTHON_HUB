names = ["Pushkar","Vivek","Geetika","Kamal","Prince"]

#names_string  = names.split(",")

import random 

numes_item = len(names)

random_choice = random.randint(0,numes_item-1)

print(f"{names[random_choice]}, is going to buy meal for us Today!")