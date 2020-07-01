from flask import Blueprint
from flask_restplus import Api


v1_blueprint = Blueprint('v1', __name__, url_prefix='/api/v1')

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

api = Api(v1_blueprint,
          doc='/docs',
          title='API for CDP Project',
          version='1.0',
          description='API for CDP Project',
          security='Bearer Auth',
          authorizations=authorizations)


from .resources.hello.hello import api as hello_ns


api.add_namespace(hello_ns)
