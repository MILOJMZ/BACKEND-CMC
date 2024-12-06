from flask import request
from backend.modelos.modelos import certificado
from flask_restful import Resource
from ..modelos import db, certificadoSchema
import cloudinary.uploader

certificado_Schema = certificadoSchema()

class Vista_certificado(Resource):
    def get(self):
        """Obtiene todos los certificados"""
        certificados = certificado.query.all()  # Trae todos los certificados
        return [certificado_Schema.dump(cert) for cert in certificados]

    def post(self):
        """Crea un nuevo certificado"""
        # Validación de los campos necesarios
        if 'id_certificado' not in request.json or 'fecha_certificado' not in request.json or \
           'estado_certificado' not in request.json or 'orden_servicio_id_orden_servicio' not in request.json:
            return {'message': 'Faltan campos necesarios'}, 400
        
        nuevo_certificado = certificado(
            id_certificado=request.json['id_certificado'],
            fecha_certificado=request.json['fecha_certificado'],
            estado_certificado=request.json['estado_certificado'],
            orden_servicio_id_orden_servicio=request.json['orden_servicio_id_orden_servicio']
        )
        
        # Gestión de la imagen
        imagen = None
        if 'imagen' in request.files:
            archivo_imagen = request.files['imagen']
            if archivo_imagen:
                try:
                    result = cloudinary.uploader.upload(archivo_imagen)
                    imagen = result['secure_url']  # Obtiene la URL segura de la imagen
                    nuevo_certificado.imagen_url = imagen  # Asigna la URL al objeto nuevo_certificado
                except Exception as e:
                    return {'message': f'Error en la subida del archivo: {str(e)}'}, 400
        
        # Guardar en la base de datos
        db.session.add(nuevo_certificado)
        db.session.commit()
        
        return certificado_Schema.dump(nuevo_certificado), 201  # Retorna el certificado creado

    def delete(self, id):
        """Elimina un certificado por su ID"""
        cert = certificado.query.get(id)
        if cert:
            db.session.delete(cert)
            db.session.commit()
            return {'message': 'Certificado eliminado'}, 204
        return {'message': 'Certificado no encontrado'}, 404


