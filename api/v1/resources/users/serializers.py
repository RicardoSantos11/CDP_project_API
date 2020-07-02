from api.v1 import api
from flask_restplus import fields


user = api.model('User', {
    '_id': fields.String(readonly=True, description='User ID'),
    'name': fields.String(required=True, description='Name of User'),
    'cpf': fields.String(required=True, description='CPF of User'),
    'datanascimento': fields.String(required=True, description='Dt. Nascto. of User'),
    'username': fields.String(required=True, description='Username of User')
})

create_user = api.inherit('User Creation', user, {
    'password': fields.String(required=True, description='User Password'),
})
