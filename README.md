# CDP_project_API
This project is the API for CDP Project.  

## Deploy

The API was deployed on Heroku:

```
URL of Swagger on Heroku: 
https://cdpapi.herokuapp.com/api/v1/docs
```

## Installing

To install and execution the API in your local machine, you will need to:

```
git clone https://github.com/RicardoSantos11/CDP_project_API.git && cd CDP_project_API

Create and activate one "virtualenv"
(using any valid form) 

pip install -r requirements.txt

python run.py
```

## Swagger

After the application goes up, open your browser on `localhost:5000/api/v1/docs` to see the self-documented interactive API.

## Project Structure

The project structure is based on the official [Scaling your project](https://flask-restplus.readthedocs.io/en/stable/scaling.html#multiple-apis-with-reusable-namespaces) doc with some adaptations (e.g `v1` folder to agroup versioned resources).

```
.
├── api
    └── helpers
        ├── __init__.py
        └── cpf.py
    └── v1
        └── resources
            └── hello
                ├── __init__.py
                └── hello.py
            └── users
                ├── __init__.py
                ├── models.py
                ├── serializers.py
                └── user.py
            └── __init__.py
        └── __init__.py
    └── __init__.py
├── .gitignore
├── CDP.postman_collection.json
├── config.py
├── Procfile
├── README.md
├── requirements.txt
├── run.py
├── runtime.txt

```

### Folders

* `api` - All the RESTful API implementation is here.
* `app/helpers` - Useful function/class helpers for all modules.
* `api/v1` - Resource agroupment for all `v1` [Namespaces](https://flask-restplus.readthedocs.io/en/stable/scaling.html#multiple-namespaces).
* `api/v1/resources` - All `v1` resources are implemented here.

### Files

* `api/__init__.py` - The Flask Application factory (`create_app()`) and it's configuration are done here. Your [Blueprints](https://flask-restplus.readthedocs.io/en/stable/scaling.html#use-with-blueprints) are registered here.
* `api/v1/__init__.py` - The Flask RESTPlus API is created here with the versioned Blueprint (e.g `v1`). Your [Namespaces](https://flask-restplus.readthedocs.io/en/stable/scaling.html#multiple-namespaces) are registered here.
* `.gitignore` - Lists files and directories which should not be added to git repository.
* `CDP.postman_collection.json` - File to import in Postman.
* `config.py` - Config file for envs, global config vars and so on.
* `Procfile` - Configuration of gunicorn (for deploy on Heroku).
* `README.md` - Instructions and informations of this API.
* `requirements.txt` - All project dependencies.
* `run.py` - The Application entrypoint.
* `runtime.py` - Set version of Python for deploy on Heroku.

### API Versioning

If you need to create another API version (like `/api/v2`), follow these steps:

First, create your `v2` API structure folder:

```
mkdir api/v2
touch api/v2/__init__.py
```

Inside your `api/v2/__init__.py` create your Blueprint:

```
from flask import Blueprint
from flask_restplus import Api

v2_blueprint = Blueprint('v2', __name__, url_prefix='/api/v2')

api = Api(v2_blueprint,
          doc='/docs',
          title='Flask App',
          version='2.0',
          description='Flask RESTful API V2')
```

Create your resources and namespaces inside `api/v2/resources` (like the `api/v1/resources`) and register them:

```
# api/v2/__init__.py

from flask import Blueprint
from flask_restplus import Api

v2_blueprint = Blueprint('v2', __name__, url_prefix='/api/v2')

api = Api(v2_blueprint,
          doc='/docs',
          title='Flask App',
          version='2.0',
          description='Flask RESTful API V2')


# Fictious resource example
from .resources.auth.login import api as auth_ns
api.add_namespace(auth_ns)

```

And finally, register your Blueprint with the Flask Application:

```
# api/__init__.py

# config code...
from api.v1 import v1_blueprint
    api.register_blueprint(v1_blueprint)

from api.v2 import v2_blueprint
    api.register_blueprint(v2_blueprint)

```

Now you have your new endpoints with the base path `/api/v2` :) !

OBS: Your swagger docs for this new API version will be under this base path too. Ex: `localhost:5000/api/v2/docs`.
