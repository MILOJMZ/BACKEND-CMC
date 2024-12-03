from flask import request
from backend.modelos.modelos import certificado
from flask_restful import Resource
from ..modelos import db, certificado, certificadoSchema

certificado_Schema = certificadoSchema()


class Vista_certificado(Resource):
    def get(self):
        return [certificado_Schema.dump(certificado) for certificado in certificado.query.all()]  
    
    def post(self):
        nuevo_certificado = certificado(id_certificado=request.json['id_certificado'],
                                     fecha_certificado=request.json['fecha_certificado'],
                                     estado_certificado=request.json['estado_certificado'],
                                     orden_servicio_id_orden_servicio=request.json['orden_servicio_id_orden_servicio'])
                                                                
        db.session.add(nuevo_certificado)
        db.session.commit()
        return certificado_Schema.dump(nuevo_certificado)


    def delete(self, id):
        certificado = certificadoSchema.query.get(id)
        if certificado:
            db.session.delete(certificado)
            db.session.commit()
            return {'message': 'Certificado eliminado'}, 204  
        return {'message': 'Certificado no encontrado'}, 404 



