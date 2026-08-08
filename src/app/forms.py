from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

# Formulario de Autenticación con validación en servidor e inserción automática de CSRF
class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField('Contrasena', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesion')

# Formulario de Publicación con validación de campos obligatorios
class PublicacionForm(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired(), Length(min=3, max=150)])
    contenido = TextAreaField('Contenido', validators=[DataRequired()])
    submit = SubmitField('Publicar')