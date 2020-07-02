from flask_restplus import Resource, Namespace
from .serializers import user, create_user
from .models import Users


api = Namespace('users', 'Users Endpoint')


@api.route('')
class UserList(Resource):

    @api.marshal_list_with(user)
    def get(self):
        """
        Get all users
        """
        return Users.get_all_users()
