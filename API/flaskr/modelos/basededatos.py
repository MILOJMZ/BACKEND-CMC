from marshmallow import fields 
from flask_sqlalchemy import SQLALchemy
import enum 

from marshmallow_sqlalchemy import SQLALchemyAutoSchema

db = SQLALchemy()

detalle_servicio_has_orden_servicio = db.Table('detalle_servicio_has_orden_servicio', \
        db.Column('id_detalle_servicio', db.Integer, db.ForeignKey('detalle_servicio.id_detalle_servicio'), primary_key=True),
        db.Column('id_orden_servicio', db.Integer, db.ForeignKey('orden_servicio.id_orden_servicio'), primary_key=True))

class rol(db.Model):
    id_rol = db.Column(db.Integer, primary_key = True)
    nombre_rol = db.Column(db.String(45))

class rep_legal(db.Model): 
    rep_id = db.Column(db.Integer, primary_key = True)
    rep_nombre = db.Column(db.String(45))
    rep_nombreusuario = db.Column(db.String(45))
    rep_direccion = db.Column(db.String(45))
    rep_telefono = db.Column(db.Integer)
    rep_contrasena = db.Column(db.String(45))
    rol_id_rol =  db.Column(db.Integer)

class categoria(db.Model): 
    id_categoria = db.Column(db.Integer, primary_key = True)
    cat_descripcion = db.Column(db.String(45))
    rep_legal_rep_id = db.Column(db.Integer)

class establecimiento(db.Model):
    id_establecimiento = db.Column(db.Integer, primary_key = True)
    correo_est = db.Column(db.String(45))
    direccion_est = db.Column(db.String(45))
    nombre_est = db.Column(db.String(45))
    rep_legal_rep_id = db.Column(db.Integer)

class orden_servicio(db.Model):
    id_orden_servicio = db.Column(db.Integer, primary_key = True)
    orden_serv_fecha = db.column(db.Date)
    orden_serv_hora = db.Column(db.String(45))
    orden_serv_precaucion = db.Column(db.String)
    rep_legal_rep_id = db.Column(db.Integer)

class tipo_servicio(db.Model):
    id_tipo_servicio = db.Column(db.Integer, primary_key = True)
    tipo_serv_suministro_emergencia = db.Column(db.string(45))
    tipo_serv_control_roedores = db.Column(db.String(45))
    tipo_serv_lavado_tanques = db.Column(db.String(45))
    tipo_serv_capacitacionSST = db.Column(db.String(45))
    tipo_serv_descripcion = db.Column(db.String(45))
    orden_servicio_id_orden_servicio = db.Column(db.Integer)
    
class detalle_servicio(db.Model):
    id_detalle_servicio = db.Column(db.Integer, primary_key = True)
    det_serv_precio = db.Column(db.Integer)
    det_serv_nombre_operario = db.Column(db.String(45))
    def_serv_cantidad_producto = db.Column(db.String(45))
    det_fin_servicio = db.Column(db.String(45))

class certificado(db.Model): 
    id_certificado = db.Column(db.Integer, primary_key = True)
    fecha_certificado = db.Column(db.Date)
    estado_certificado = db.Column(db.String(45))
    orden_servicio_id_orden_servicio = db.Column(db.Integer)

    class ficha_tecnica(db.Model):
        fct_producto_aplicado = db.Column(db.String(45), primary_key = True)
        fct_dosis = db.Column(db.String(45))
        fct_ingrediente_activo = db.Column(db.String(45))
        certificado_id_certificado = db.Column(db.Integer)
        detalle_servicio_id_detalle_servicio = db.Column(db.Integer)
