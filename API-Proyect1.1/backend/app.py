from backend.modelos import db
from backend import create_app
from flask_restful import Api
from flask_cors import CORS
from .vistas.vistas_usuarios import Vista_rep_legal
from .vistas.vista_certificado import Vista_certificado

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()
CORS(app)

from flask import Flask, request

api=Api(app)

api.add_resource(Vista_rep_legal,'/usuarios')

api.add_resource(Vista_certificado,'/certificados')





