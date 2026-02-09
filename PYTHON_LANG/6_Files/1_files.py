

# file = open("myfile.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("myfile.txt", mode = "r") as file: #read mode
    contents = file.read()
    print(contents)

# with open("myfile.txt",mode= "w") as file:  #write mode , delete everything then add new text
#     file.write("I am a AI Developer")


with open("myfile.txt",mode= "a") as file: #append add new text at existing file
    file.write("\nI am a AI Developer")

with open("newfile.txt",mode= "w") as file: #create new file
    file.write("\nnewtext.")

