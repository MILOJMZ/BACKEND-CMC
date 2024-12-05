from flask import request
from backend.modelos.modelos import certificado
from flask_restful import Resource
from ..modelos import db, certificado, CertificadoSchema

certificado_Schema = CertificadoSchema()


class Vista_certificado(Resource):
    def get(self):
        return [certificado_Schema.dump(certificado) for certificado in certificado.query.all()]
    def post(self):
        nuevo_certificado = certificado(id_certificado=request.json['id_certificado'],
                             fecha_certificado=request.json['fecha_certificado'],
                             estado_certificado=request.json['estado_certificado'],
                             orden_servicio_id_orden_servicio=request.json['orden_servicio_id_orden_servicio'])  
    imagen= None
     if 'imagen' in request.files:
         archivo_imagen= request.files['imagen']
         if archivo_imagen:
             try:
                 result=cloudinary.uploader.upload(archivo_imagen)
                 imagen=result['secure_url']
             except Exception as e:
                 return str(e), 400  # Error en la subida del archivo
                                    
                                    
        db.session.add(nuevo_certificado)
        db.session.commit()
        return certificado_Schema.dump(nuevo_certificado)


    def delete(self, id):
        certificado = CertificadoSchema.query.get(id)
        if certificado:
            db.session.delete(certificado)
            db.session.commit()
            return {'message': 'Certificado eliminado'}, 204  
        return {'message': 'Certificado no encontrado'}, 404 



