import uuid
from flask import current_app
from flask_restplus import abort


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
        user_ref = set_users()

        try:
            user_json = {
                "_id": str(uuid.uuid4()),
                "name": user.get('name'),
                "email": user.get('email'),
                "phone": user.get('phone'),
                "cpf": user.get('cpf'),
                "birth_date": user.get('birth_date'),
                "brand": user.get('brand'),
                "source": user.get('source')
            }
            if not user_ref.insert_one(user_json).inserted_id:
                abort(422, 'Cannot create user')
            return user_json
        except Exception as e:
            return f"An Error Ocurred: {e}"

    @classmethod
    def delete_user(cls, id):
        users_ref = set_users()

        if users_ref.delete_one({'_id': id}).deleted_count:
            return '', 204
        abort(404, 'User not found')
