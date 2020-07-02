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
    def insert_user(user):
        pass
