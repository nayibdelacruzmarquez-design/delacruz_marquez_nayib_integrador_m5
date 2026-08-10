from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# Definición de roles de usuario para el control de acceso (RBAC)
class Role:
    ADMIN = 'admin'
    USER = 'user'


# Modelo de Usuario
class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    rol = db.Column(db.String(20), nullable=False, default=Role.USER)

    # Relación 1 a N con Publicacion
    publicaciones = db.relationship('Publicacion', backref='autor', lazy='select')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'rol': self.rol
        }


# Modelo de Publicación (Recurso principal de la API REST)
class Publicacion(db.Model):
    __tablename__ = 'publicaciones'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    # Clave foránea
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'contenido': self.contenido,
            'fecha_creacion': self.fecha_creacion.isoformat() if self.fecha_creacion else None,
            'usuario_id': self.usuario_id,
            'autor': self.autor.username if self.autor else None
        }