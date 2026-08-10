import os
from flask import Flask, jsonify, request

from models import db, Usuario, Publicacion, Role

app = Flask(__name__)

# Configuración de seguridad y base de datos
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'clave_secreta_integrador_m5')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.before_request
def inicializar_bd():
    """Inicializa las tablas e inserta registros de prueba si la BD está vacía."""
    db.create_all()
    if not Usuario.query.first():
        admin = Usuario(username='admin', password='adminpassword', rol=Role.ADMIN)
        user = Usuario(username='usuario', password='userpassword', rol=Role.USER)
        db.session.add_all([admin, user])
        db.session.commit()

        p1 = Publicacion(
            titulo='Primera Publicación REST',
            contenido='Contenido de prueba para la API REST.',
            usuario_id=admin.id
        )
        p2 = Publicacion(
            titulo='Segunda Publicación REST',
            contenido='Optimizando consultas con SQLAlchemy.',
            usuario_id=user.id
        )
        db.session.add_all([p1, p2])
        db.session.commit()


# Helper para verificar credenciales de autorización
def obtener_usuario_autenticado():
    """
    Verifica el header 'Authorization'.
    Retorna el objeto Usuario o un código de error (401 o 403).
    """
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return None, (jsonify({'error': 'No autorizado. Se requiere token o credencial en el header Authorization'}), 401)

    # Simulación de token/credencial: 'Bearer admin-token' o 'Bearer user-token'
    token = auth_header.replace('Bearer ', '').strip()
    if token == 'admin-token':
        user = Usuario.query.filter_by(rol=Role.ADMIN).first()
        return user, None
    elif token == 'user-token':
        user = Usuario.query.filter_by(rol=Role.USER).first()
        return user, None
    else:
        return None, (jsonify({'error': 'Credencial inválida o expirada'}), 401)


# ==========================================
# RUTAS DE LA API REST (JSON)
# ==========================================

# 1. LISTAR con Paginación y prevención N+1 (GET)
@app.route('/api/v1/publicaciones', methods=['GET'])
def get_publicaciones():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # Consulta con joinedload para evitar N+1
    query = Publicacion.query.options(db.joinedload(Publicacion.autor))
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        'data': [p.to_dict() for p in pagination.items],
        'total': pagination.total,
        'page': pagination.page,
        'pages': pagination.pages,
        'has_next': pagination.has_next,
        'has_prev': pagination.has_prev
    }), 200


# 2. DETALLE de un recurso (GET)
@app.route('/api/v1/publicaciones/<int:pub_id>', methods=['GET'])
def get_publicacion_detalle(pub_id):
    publicacion = Publicacion.query.options(db.joinedload(Publicacion.autor)).get(pub_id)
    if not publicacion:
        return jsonify({'error': 'Publicación no encontrada'}), 404

    return jsonify({'data': publicacion.to_dict()}), 200


# 3. CREACIÓN con Validación de entrada (POST)
@app.route('/api/v1/publicaciones', methods=['POST'])
def crear_publicacion():
    user, error = obtener_usuario_autenticado()
    if error:
        return error  # Retorna 401 si no hay credenciales

    data = request.get_json() or {}

    # Validación de entrada
    if not data.get('titulo') or not str(data.get('titulo')).strip():
        return jsonify({'error': 'El campo "titulo" es obligatorio'}), 400
    if not data.get('contenido') or not str(data.get('contenido')).strip():
        return jsonify({'error': 'El campo "contenido" es obligatorio'}), 400

    nueva_pub = Publicacion(
        titulo=data['titulo'].strip(),
        contenido=data['contenido'].strip(),
        usuario_id=user.id
    )
    db.session.add(nueva_pub)
    db.session.commit()

    return jsonify({
        'message': 'Publicación creada exitosamente',
        'data': nueva_pub.to_dict()
    }), 201


# 4. ACTUALIZACIÓN protegida (PUT)
@app.route('/api/v1/publicaciones/<int:pub_id>', methods=['PUT'])
def actualizar_publicacion(pub_id):
    user, error = obtener_usuario_autenticado()
    if error:
        return error  # Retorna 401 si no tiene token

    publicacion = Publicacion.query.get(pub_id)
    if not publicacion:
        return jsonify({'error': 'Publicación no encontrada'}), 404

    # Control de Acceso (403 Forbidden si intenta modificar un recurso ajeno)
    if user.rol != Role.ADMIN and publicacion.usuario_id != user.id:
        return jsonify({'error': 'Prohibido. No tienes permisos para modificar recursos ajenos'}), 403

    data = request.get_json() or {}
    if 'titulo' in data:
        publicacion.titulo = data['titulo']
    if 'contenido' in data:
        publicacion.contenido = data['contenido']

    db.session.commit()
    return jsonify({
        'message': 'Publicación actualizada correctamente',
        'data': publicacion.to_dict()
    }), 200


# 5. ELIMINACIÓN protegida (DELETE)
@app.route('/api/v1/publicaciones/<int:pub_id>', methods=['DELETE'])
def eliminar_publicacion(pub_id):
    user, error = obtener_usuario_autenticado()
    if error:
        return error  # Retorna 401 si no hay token

    publicacion = Publicacion.query.get(pub_id)
    if not publicacion:
        return jsonify({'error': 'Publicación no encontrada'}), 404

    # Control de Acceso (403 Forbidden si el recurso pertenece a otro usuario)
    if user.rol != Role.ADMIN and publicacion.usuario_id != user.id:
        return jsonify({'error': 'Prohibido. No tienes permisos para eliminar recursos ajenos'}), 403

    db.session.delete(publicacion)
    db.session.commit()
    return jsonify({'message': 'Publicación eliminada exitosamente'}), 200


# Endpoint de salud para la raíz /
@app.route('/', methods=['GET'])
def root():
    return jsonify({
        'status': 'online',
        'service': 'API REST Integrador Módulo 5',
        'version': '1.0.0',
        'endpoints': {
            'listar': 'GET /api/v1/publicaciones',
            'detalle': 'GET /api/v1/publicaciones/<id>',
            'crear': 'POST /api/v1/publicaciones',
            'actualizar': 'PUT /api/v1/publicaciones/<id>',
            'eliminar': 'DELETE /api/v1/publicaciones/<id>'
        }
    }), 200


if __name__ == '__main__':
    app.run(debug=True)