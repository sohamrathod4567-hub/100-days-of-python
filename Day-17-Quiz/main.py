class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        print("New user being created")
user1 = User("001" , "soham")
user2 = User("002" , "nikolas jackson")
print(user1.id)
print(user1.username)
print(user1.followers)
