from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# Definición de roles de usuario para el control de acceso (RBAC)
class Role:
    ADMIN = 'admin'
    USER = 'user'


# Modelo de Usuario (Requisito 1 de la entrega)
class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    rol = db.Column(db.String(20), nullable=False, default=Role.USER)

    # Relación 1 a N con el modelo Publicacion (evita redundancia)
    publicaciones = db.relationship('Publicacion', backref='autor', lazy='select')


# Modelo de Publicación (Requisito 2 de la entrega: >= 2 modelos relacionados)
class Publicacion(db.Model):
    __tablename__ = 'publicaciones'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    # Clave foránea que vincula la publicación con su autor
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)