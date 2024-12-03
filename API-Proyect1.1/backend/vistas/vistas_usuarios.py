from flask import request
from ..modelos.modelos import rep_legal
from flask_restful import Resource
from ..modelos import db, RepLegalSchema
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

rep_legal_schema = RepLegalSchema()

class VistaRepLegal(Resource):
    def get(self):
        """Obtiene todos los representantes legales"""
        return [rep_legal_schema.dump(rep_legal) for rep_legal in rep_legal.query.all()]

    def post(self):
        """Crea un nuevo representante legal o realiza la autenticación"""
        if 'nombre_usuario' in request.json:

            nuevo_rep_legal = rep_legal(
                nombre_usuario=request.json['nombre_usuario'],
                contrasena_hash=generate_password_hash(request.json['contrasena'])  # Use contrasena_hash from your model
            )
            db.session.add(nuevo_rep_legal)
            db.session.commit()
            access_token = create_access_token(identity=nuevo_rep_legal.id)
            return {'mensaje': 'Usuario creado exitosamente', 'token_de_acceso': access_token}, 201
        else:

            rep_nombre_usuario = request.json["nombre_usuario"]
            rep_contrasena = request.json["contrasena"]
            rep_legal = rep_legal.query.filter_by(nombre_usuario=rep_nombre_usuario).first()
            if rep_legal and check_password_hash(rep_legal.contrasena_hash, rep_contrasena):  # Use contrasena_hash for password comparison
                access_token = create_access_token(identity=rep_legal.id)
                return {'mensaje': 'Inicio de sesión exitoso', 'token_de_acceso': access_token}, 200
            else:
                return {'mensaje': 'Nombre de usuario o contraseña incorrectos'}, 401

    def put(self, id):
        """Actualiza un representante legal existente"""
        rep_legal = rep_legal.query.get(id)
        if not rep_legal:
            return {'mensaje': 'Representante legal no encontrado'}, 404



        db.session.commit()
        return rep_legal_schema.dump(rep_legal)

    def delete(self, id):
        """Elimina un representante legal"""
        rep_legal = rep_legal.query.get(id)
        if not rep_legal:
            return {'mensaje': 'Representante legal no encontrado'}, 404

        db.session.delete(rep_legal)
        db.session.commit()
        return {'mensaje': 'Representante legal eliminado exitosamente'}, 204