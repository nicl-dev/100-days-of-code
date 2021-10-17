class User:
    """Creating new user.
    """
    def __init__(self, user_id, username):
        # initialize attributes
        self.user_id = user_id
        self.username = username
        self. followers = 0

user_1 = User("001", "ragemoody")
user_2 = User("002", "Nicole")

print(user_2.followers)