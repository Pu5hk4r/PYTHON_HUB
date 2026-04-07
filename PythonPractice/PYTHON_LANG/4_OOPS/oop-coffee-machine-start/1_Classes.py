class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

# Creating an instance of User outside the class definition
user_1 = User(-1, "Pushkar")
print(user_1.id, user_1.username, user_1.followers)

user_2= User(2, "Sharma")
print(user_2.id, user_2.username, user_2.followers)