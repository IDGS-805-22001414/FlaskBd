from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import CSRFProtect  
from config import DevelopmentConfig
import forms
from models import db, Alumnos
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Inicializar la base de datos correctamente
db.init_app(app)

# Asociar CSRF a la aplicación
csrf = CSRFProtect(app)

# -------- Rutas --------
@app.route("/", methods=['GET', 'POST'])
@app.route("/index")
def index():
    create_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()
    return render_template("index.html", form=create_form, Alumnos=alumno)

@app.route("/detalles", methods=['GET', 'POST'])
def detalles():
    create_form = forms.UserForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum1:  # Verificar si el alumno existe
            return render_template("detalles.html", form=create_form, nombre=alum1.nombre, apellido=alum1.apaterno, email=alum1.email)
        else:
            flash("Alumno no encontrado", "error")
            return redirect(url_for('index'))

@app.route("/Alumnos1", methods=['GET', 'POST'])
def Alumnos1():
    create_form = forms.UserForm2(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre=create_form.nombre.data, apaterno=create_form.apaterno.data, email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('Alumnos1.html', form=create_form)

@app.route("/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum1:
            create_form.id.data = id
            create_form.nombre.data = alum1.nombre.strip()
            create_form.apaterno.data = alum1.apaterno
            create_form.email.data = alum1.email
        else:
            flash("Alumno no encontrado", "error")
            return redirect(url_for('index'))

    if request.method == 'POST':
        id = create_form.id.data
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum1:
            alum1.nombre = create_form.nombre.data.strip()
            alum1.apaterno = create_form.apaterno.data
            alum1.email = create_form.email.data
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('modificar.html', form=create_form)

@app.route("/eliminar", methods=['GET', 'POST'])
def eliminar(): 
    create_form = forms.UserForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum1:
            create_form.id.data = id
            create_form.nombre.data = alum1.nombre
            create_form.apaterno.data = alum1.apaterno
            create_form.email.data = alum1.email
        else:
            flash("Alumno no encontrado", "error")
            return redirect(url_for('index'))

    if request.method == 'POST':
        id = create_form.id.data
        alum = Alumnos.query.get(id)
        if alum:
            db.session.delete(alum)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('eliminar.html', form=create_form)

@app.route("/test_db")
def test_db():
    alumnos = Alumnos.query.all()
    return {"total": len(alumnos), "datos": [alumno.nombre for alumno in alumnos]}


# -------- Iniciar el servidor correctamente --------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear tablas si no existen
    
    app.run(debug=True)
