from flask import Flask
from flask import Flask
import cloudinary
import cloudinary.uploader
import cloudinary.api


def create_app():
    app = Flask(__name__)

    # Configuración de Cloudinary desde variables de entorno
    cloudinary.config()
    cloud_name='dpj43nn12',
    api_key='616368946578119',
    api_secret='vUq-UcvIEleLUWcm5GvXfWa-ST8'


def create_app(config_name=None):
    app = Flask(__name__)

    # Configuración de la base de datos
    USER_DB = 'root'
    PASS_DB = ''
    URL_DB = 'localhost'
    NAME_DB = 'cmc'
    FULL_URL_DB = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

    app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    #JWT
    app.config['JWT_SECRET_KEY'] = 'frase-secret'
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app

import os
from flask import Flask
import cloudinary
import cloudinary.uploader
import cloudinary.api


def create_app():
    app = Flask(__name__)

    # Configuración de Cloudinary desde variables de entorno
    cloudinary.config(
        cloud_name=os.getenv('dpj43nn12'),
        api_key=os.getenv('616368946578119'),
        api_secret=os.getenv('vUq-UcvIEleLUWcm5GvXfWa-ST8')
    )

    # Configuración de la base de datos desde variables de entorno
    USER_DB = os.getenv('DB_USER', 'root')
    PASS_DB = os.getenv('DB_PASS', '')
    URL_DB = os.getenv('DB_URL', 'localhost')
    NAME_DB = os.getenv('DB_NAME', 'cmc')
    FULL_URL_DB = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

    app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configuración de JWT desde variables de entorno
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'frase-secret')
    app.config['PROPAGATE_EXCEPTIONS'] = True

    return app

