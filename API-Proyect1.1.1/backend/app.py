from flask import Flask
from backend.modelos import db
from backend import create_app
from flask_restful import Api
from flask_cors import CORS
from .vistas.vistas_usuarios import VistaRepLegal
from .vistas.vista_certificado import Vista_certificado
from .vistas.vista_rol import Vista_rol
from flask_migrate import Migrate

app = create_app()
app_context = app.app_context()
app_context.push()
Migrate(app, db)
db.init_app(app)
db.create_all()
CORS(app)



api=Api(app)

api.add_resource(VistaRepLegal,'/usuarios')

api.add_resource(Vista_certificado,'/certificados')

api.add_resource(Vista_rol, '/roles')





