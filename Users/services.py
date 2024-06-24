from Users.repository import UserRepository


user_instance = UserRepository()


def create_user(user_data):
    new_user = user_instance.add(user_data.username, user_data.email, user_data.password)
    return new_user
