from flask import request
from flask_restful import Resource
from .modelos import db, cmc, cmcSchema
certificadoschema()

certificadoschema = cmcSchema()

class Buscar(Resource):
    def get(self): 
        certificados = BuscarC.query.all()
        return [certificadoschema.dump(certificado) for certificado in certificados]

class AgregarCertificado(Resource):
    def post(self):  
        nuevo_certificado = BuscarC(
            id_certificado=request.json['id_certificado'],
            fecha_certificado=request.json['fecha_certificado'],
            estado_certificado=request.json['estado_certificado'],
            orden_servicio_id_orden_servicio=request.json['orden_servicio_id_orden_servicio'],
        )
        
        db.session.add(nuevo_certificado)
        db.session.commit()
        return certificado.dump(nuevo_certificado), 201 

class EliminarCertificado(Resource):
    def delete(self, id):
        certificado = BuscarC.query.get(id)
        if certificado:
            db.session.delete(certificado)
            db.session.commit()
            return {'message': 'Certificado eliminado'}, 204  
        return {'message': 'Certificado no encontrado'}, 404 

    from .modelos import db, Usuario, UsuarioSchema