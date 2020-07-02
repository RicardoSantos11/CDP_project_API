from flask import current_app


def set_users():
    db = current_app.config.get('DB', None)
    users_ref = db['users']
    return users_ref


class Users:

    def __init__(self):
        pass

    @staticmethod
    def get_all_users():
        users_ref = set_users()

        all_users = [user for user in users_ref.find()]
        return all_users

    @staticmethod
    def get_user(id):
        user_ref = set_users()

        user = user_ref.find_one({'_id': id})
        if user:
            return user

        return None


    @staticmethod
    def insert_user(user):
        pass
