from api.v1 import api
from flask_restplus import fields


user = api.model('User', {
    '_id': fields.String(readonly=True, description='User ID'),
    'name': fields.String(required=True, description='Name of User'),
    'email': fields.String(required=True, description='Email of User'),
    'mobile_phone': fields.String(required=True, description='Phone of User'),
    'cpf': fields.String(required=True, description='CPF of User'),
    'birth_date': fields.Date(required=True, description='Birth Date of User'),
    'brand': fields.String(required=True, description='Brand of User'),
    'source': fields.String(required=True, description='Source of User'),
    'privacy_consent': fields.String(required=True, description='privacy_consent of User'),
    'media_consent': fields.String(required=True, description='media_consent of User'),
    'reg_date': fields.String(required=True, description='reg_date of User')
})
