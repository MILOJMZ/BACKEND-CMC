from flask import request
from backend.modelos.modelos import rol
from flask_restful import Resource
from ..modelos import db, rol, RolSchema

rol_Schema = RolSchema()

class Vista_rol(Resource):
     def get(self):
        return [rol_Schema.dump(certificado) for certificado in rol.query.all()]  
     

    
     def put(self, id):
        rep_legal = rep_legal.query.get(id)
        if not rep_legal:
            return 'Usuario no encontrado', 404