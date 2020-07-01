from flask_restplus import Resource, Namespace


api = Namespace('hello', 'Hello endpoint')


@api.route('/')
class Hello(Resource):

    def get(self):
        """
        Return msg "I'm a a API for CDP Project"
        """
        return {"msg": "I'm a API for CDP Project."}, 200
