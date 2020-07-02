import os
import sys
from pymongo import MongoClient

class BaseConfig:

    DEBUG = True
    RESTPLUS_VALIDATE = True
    ERROR_INCLUDE_MESSAGE = False
    RESTPLUS_MASK_SWAGGER = False

    try:
        # Conecting Cosmos DB
        MONGO_URI = os.getenv('MONGO_URI')
        client = MongoClient(MONGO_URI)

        # TODO: For some unknown reason, it is not recognizing the environment variable.
        # DB = os.getenv('DB_MONGO')
        DB = client['CDP_project']
    except Exception as e:
        print(e)
        sys.exit()


class ProdConfig(BaseConfig):

    DEBUG = False


class DevConfig(BaseConfig):

    pass
