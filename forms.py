from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField
from wtforms import validators

class UserForm(FlaskForm):  # Cambia "Form" por "FlaskForm"
    nombre = StringField('nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=10, message='Ingrese un nombre válido')
    ])
    apaterno = StringField('apaterno')
    amaterno = StringField('amaterno')
    email = EmailField('email', [validators.Email(message='Ingrese un correo válido')])
    edad = IntegerField('edad')

class UserForm2(FlaskForm):  # Cambia "Form" por "FlaskForm"
    id = IntegerField('id', [
        validators.NumberRange(min=1, max=20, message='Valor no válido')
    ])
    nombre = StringField('nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.Length(min=4, max=20, message='Requiere mínimo 4 y máximo 20 caracteres')
    ])
    apaterno = StringField('apaterno', [
        validators.DataRequired(message='El apellido es requerido')
    ])
    email = EmailField('correo', [
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo válido')
    ])
