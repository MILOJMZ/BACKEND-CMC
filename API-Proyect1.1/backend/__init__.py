from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy


# Inicializar exte

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


