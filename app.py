from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import CSRFProtect  # Corrección de importación
from config import DevelopmentConfig
import forms
from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Asociar CSRF a la aplicación
csrf = CSRFProtect(app)

@app.route("/", methods=['GET', 'POST'])
@app.route("/index")
def index():
    create_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()
    return render_template("index.html", form=create_form, Alumnos=alumno)

@app.route("/detalles", methods=['GET', 'POST'])
def detalles():
    create_form=forms.UserForm2(request.form)
    if request.method ==  'GET':
        id=request.args.get('id')
    alum1=db.session.query(Alumnos).filter(Alumnos.id).first()
    nom=alum1.nombre
    ape=alum1.apellido
    email=alum1.email

    return render_template("detalles.html",form=create_form,nombre=nom,apellido=ape,email=email)

@app.route("/Alumnos1" , methods=['GET' , 'POST'])
def Alumnos1():
    create_form=forms.UserForm2(request.form)
    if request.method=='POST':
        alum=Alumnos(nombre=create_form.nombre.data,
                     apaterno=create_form.apaterno.data,
                     email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        return render_template('Alumnos1.html',form=create_form)
        
if __name__ == '__main__':
    # Inicializar base de datos correctamente
    db.init_app(app)
    
    with app.app_context():
        db.create_all()  # Crear tablas si no existen
    
    app.run(debug=True)
