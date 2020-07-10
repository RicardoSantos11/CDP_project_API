import datetime
import json
import uuid
from bson.json_util import dumps
from flask import current_app
from flask_restplus import abort
from validate_email import validate_email

from api.helpers.cpf import Cpf


def set_users():
    db = current_app.config.get('DB', None)
    users_ref = db['users']
    return users_ref


def under_age(date):
    is_under_age = False
    year = datetime.datetime.now().date().year
    year_user = datetime.datetime.strptime(date, '%d/%m/%Y').year
    if (year - year_user) < 18:
        is_under_age = True
    return is_under_age


def basic_validations(user):
    error = None
    if not ('name' in user) or len(user.get('name')) < 3:
        error = 'Field name is missing or invalid.'
    elif not ('surname' in user) or len(user.get('surname')) < 3:
        error = 'Field surname is missing or invalid.'
    elif not ('email' in user):
        error = 'Field email is missing.'
    elif not validate_email(email_address=user.get('email'), check_mx=False):
        error = 'Invalid email.'
    elif not ('mobile_phone' in user) or len(user.get('mobile_phone')) < 9:
        error = 'Field mobile_phone is missing or invalid.'
    elif not ('birth_date' in user) or len(user.get('birth_date')) < 8:
        error = 'Field birdth_date is missing or invalid.'
    elif under_age(user.get('birth_date')):
        error = 'User under age not allowed.'
    elif not ('source' in user) or len(user.get('source')) < 3:
        error = 'Field source is missing or invalid.'
    elif not ('privacy_consent' in user):
        error = 'Field privacy_consent is missing.'
    elif not user.get('privacy_consent') == True: # Is necessary be TRUE
        error = 'User did not grant permission.'
    elif not ('media_consent' in user):
        error = 'Field media_consent is missing.'
    elif ('cpf' in user): # This information is optional
        if not Cpf.validate(Cpf.format(user.get('cpf'))): # Is necessary come with MASK (xxx.xxx.xxx-xx)
            error = 'Invalid CPF.'
    return error


def date_in(date):
    date_str = date + ' 00:00:00'
    date_f = datetime.datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
    return date_f


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
        error = basic_validations(user)
        if error:
            abort(422, error)

        user_ref = set_users()
        try:
            user['_id'] = str(uuid.uuid4())
            user['cpf'] = Cpf.remove_mask(user.get('cpf'))
            user['birth_date'] = date_in(user.get('birth_date'))
            user['reg_date'] = datetime.datetime.now()

            if not user_ref.insert_one(user).inserted_id:
                abort(422, 'Cannot create user')

            user.pop('birth_date')
            user.pop('reg_date')

            return json.loads(dumps(user))
        except Exception as e:
            return f"An Error Ocurred: {e}"

    @classmethod
    def update_user(cls, id, data):
        user_ref = set_users()

        if not cls.get_user(id):
            abort(404, 'User not found')

        if user_ref.update_one({'_id': id}, {'$set': data}):
            return '', 204
        abort(422, 'No user updated')

    @classmethod
    def delete_user(cls, id):
        user_ref = set_users()

        if user_ref.delete_one({'_id': id}).deleted_count:
            return '', 204
        abort(404, 'User not found')
