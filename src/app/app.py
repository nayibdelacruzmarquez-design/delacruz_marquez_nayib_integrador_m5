import os
from flask import Flask, render_template, redirect, url_for, flash, session, request

# Importación directa de modelos y formularios
from models import db, Usuario, Publicacion, Role
from forms import LoginForm, PublicacionForm

app = Flask(__name__)

# Configuración de seguridad y base de datos
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'clave_secreta_integrador_m4')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.before_request
def inicializar_bd():
    """Inicializa las tablas e inserta usuarios por defecto si la base de datos esta vacia."""
    db.create_all()
    if not Usuario.query.first():
        admin = Usuario(username='admin', password='adminpassword', rol=Role.ADMIN)
        user = Usuario(username='usuario', password='userpassword', rol=Role.USER)
        db.session.add_all([admin, user])
        db.session.commit()

        post = Publicacion(
            titulo='Proyecto Integrador Módulo 4',
            contenido='Bienvenido a la aplicación web del proyecto integrador.',
            usuario_id=admin.id
        )
        db.session.add(post)
        db.session.commit()


@app.route('/')
def index():
    """Ruta principal: Optimización ORM con joinedload para evitar consultas N+1."""
    publicaciones = Publicacion.query.options(db.joinedload(Publicacion.autor)).all()
    return render_template('index.html', publicaciones=publicaciones)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Ruta de autenticación y manejo de sesión por roles."""
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            session['user_id'] = user.id
            session['username'] = user.username
            session['rol'] = user.rol
            flash('Inicio de sesion exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciales invalidas', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """Cierre de sesión de usuario."""
    session.clear()
    flash('Sesion cerrada correctamente', 'info')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)