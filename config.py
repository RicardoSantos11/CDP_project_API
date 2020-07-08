import os
import sys
import logging
from logging.config import dictConfig
from pymongo import MongoClient


logger = logging.getLogger(__name__)

dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[%(levelname)s] - [%(asctime)s] - %(name)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
        }
    },
    "loggers": {
        "werkzeug": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"]
    }
})


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
    except KeyError as key:
        logger.critical(f'{key} env var is missing !')
        sys.exit()
    except Exception as e:
        print(e)
        sys.exit()


class ProdConfig(BaseConfig):

    DEBUG = False


class DevConfig(BaseConfig):

    pass
