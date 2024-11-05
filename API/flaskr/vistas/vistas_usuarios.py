from flask import request
from flask_restful import Resource
from .modelos import db, cmc, cmcSchema
rep_legal_schema = ()


class VistaUsuario(Resource):
    def get(self):
        return [rep_legal_schema.dump(rep_legal) for rep_legal in Usuario.query.all()]

    def post(self):
        nuevo_rep_legal = rep_legal(rep_id = request.json['cedula_usuario'],
                                rep_nombre = request.json ['nombre']
                                rep_nombreusuario = request.json ['nombre_usuario'],
                                rep_contrasena = request.json['rep_contrasena'],    
                                rep_direccion= request.json['rep_direccion']
                                rep_telefono = request.json['rep_telefono'],
                                rol_id_rol = request.json['rol_id_rol'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        return rep_legal_schema.dump(nuevo_usuario)
       

    def put(self, id):
        rep_legal = rep.legal.query.get(id)
        if not rep_legal:
            return 'Usuario no encontrado', 404
       
        rep_legal.rep_id = request.json.get('rep_id', rep_legal.rep_id)
        rep_legal.rep_nombre = request.json.get('rep_nombre',rep_legal.rep_nombre)
        rep_legal.rep_nombreusuario = request.json.get('rep_nombreusuario', rep_legal.rep_nombreusuario)
        rep_legal.rep_contrasena = request.json.get('rep_contrasena', rep_legal.rep_contrasena)
        rep_legal.rep_direccion = request.json.get('rep_direccion', rep_legal.rep_direccion)
        rep_legal.telefono_usuario = request.json.get('rep_telefono', rep_legal.rep_telefono)
        rep_legal.rol_id_rol = request.json.get('rol_id_rol', rep_legal.rol_id_rol)
 
    def delete(self, id):
        rep_legal = rep_legal.query.get(id)
        if not rep_legal:
            return 'Usuario no encontrado', 404
       
        db.session.delete(rep_legal)
        db.session.commit()
        return 'El usuario fue eliminado' 