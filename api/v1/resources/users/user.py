from flask_restplus import Resource, Namespace
from .serializers import user
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

    @api.marshal_with(user, code=201)
    @api.expect(user)
    @api.doc(responses={
        400: 'Input payload validation failed',
        422: 'Cannot create user',
        500: 'Internal Server Error'
    })
    def post(self):
        """
        Creates a new user
        """
        return Users.insert_user(api.payload), 201


@api.route('/id/<string:id>')
class UserId(Resource):

    @api.marshal_with(user)
    @api.doc(responses={
        200: 'OK',
        404: 'User not found',
        500: 'Internal Server Error'
    }, params={'id': 'User ID'})
    def get(self, id):
        """
        Get User by ID
        """
        user = Users.get_user(id)
        if not user:
            api.abort(404, 'User not found')
        return user, 200

    @api.doc(responses={
        204: 'No content',
        404: 'User not found',
        500: 'Internal Server Error'
    }, params={'id': 'User ID'})
    def delete(self, id):
        """
        Deletes user by ID
        """
        return Users.delete_user(id)

    @api.expect(user)
    @api.doc(responses={
        204: 'No content',
        400: 'Input payload validation failed',
        422: 'No user updated',
        500: 'Internal Server Error'
    }, params={'id': 'user ID'})
    def put(self, id):
        """
        Updates the user
        """
        return Users.update_user(id, api.payload)
