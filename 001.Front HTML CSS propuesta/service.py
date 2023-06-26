#todo lo relacionado con del servidor va aquí

#importación del framework
from flask import Flask, render_template, request, redirect, url_for, flash, session
#flash se ocupa para poder ...
from flask_mysqldb import MySQL
#Se importa para desmenuzar la fecha 
from datetime import datetime 
# from .globals import session

#inicialización del APP (servidor)
app=Flask(__name__)

# configuración de la conexión a base de datos.
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root' 
#Laptop
app.config['MYSQL_PASSWORD']=''
#Desktop
#app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='db_clinica_s181'
esquema = 'db_clinica_s181'
#Se agrega para evitar RuntimeError: The session is unavailable because no secret key was set.
app.secret_key='mysecretkey'
mysql = MySQL(app)
# si es posible conectarse a dos bases de datos

#Declaración de la inicialización de las rutas. Ésta le pertenece a http://localhost:5000
#Ruta '/' es la ruta principal
#El archivo principal de las interfaces debe tener el 'index'
@app.route('/')
def iniciarLogin():
    return render_template('login.html')

@app.route('/menu-principal')
def iniciarMenuPrincipal():
    return render_template('menu-principal.html')

@app.route('/admon-medicos-registrar')
def iniciarRegistrarMedico():
    return render_template('admon-medicos-registrar.html')

@app.route('/registrar-perfil-paciente')
def iniciarRegistrarPaciente():
    return render_template('perfil-paciente-registrar.html')

@app.route('/actualizar-perfil-paciente')
def iniciarActualizarPaciente():
    return render_template('perfil-paciente-actualizar.html')

@app.route('/consultar-perfil-paciente')
def iniciarConsultarPaciente():
    return render_template('perfil-paciente-consultar.html')

#Método de trabajo POST que trabaja por detrás de lo que ve el usuario
@app.route('/registrar-perfil-paciente', methods=['POST'])
def registrarPaciente():
    if request.method == 'POST':

        #Pasamos a variables el contenido de los input, les ponemos una "v" de variable
        vNombreCompleto = request.form['txtNombreCompleto']
        vFechaNacimiento = request.form['dateFechaNacimiento']
        vEmail = request.form['txtEmail']
        vTelefono = request.form['txtTelefono']
        vGenero = request.form['txtGenero']
        vOcupacion = request.form['txtOcupacion']
        vTipoSangre = request.form['txtTipoSangre']
        vPeso = request.form['txtPeso']
        vAltura = request.form['txtAltura']
        vTipoIdentificacion = request.form['txtTipoIdentificacion']
        vNumeroIdentificacion = request.form['numberNumeroIdentificacion']
        vDireccionPaciente = request.form['txtDireccionPaciente']
        vPersonaContacto = request.form['txtPersonaContacto']
        vParentescoPaciente = request.form['txtParentescoPaciente']
        vTelefonoFamiliar = request.form['txtTelefonoFamiliar']
        vEnfermedadesCronicas = request.form['txtEnfermedadesCronicas']
        vAlergias = request.form['txtAlergias']
        vAntecedentesFamiliares = request.form['txtAntecedentesFamiliares']
        vDatosMedicos = request.form['txtDatosMedico']
        print("Los datos recogidos desde front son : {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(vNombreCompleto, vFechaNacimiento, vEmail, vTelefono, vGenero, vOcupacion, vTipoSangre, vPeso, vAltura, vTipoIdentificacion, vNumeroIdentificacion, vDireccionPaciente, vPersonaContacto, vParentescoPaciente, vTelefonoFamiliar, vEnfermedadesCronicas, vAlergias, vAntecedentesFamiliares, vDatosMedicos))
        
        if vGenero == 'Masculino':
            vGenero = 1
        elif vGenero == 'Femenino':
            vGenero = 2
        else: 
            vGenero = 3
            
        date_object = datetime.strptime(vFechaNacimiento, '%Y-%m-%d')
        vFechaNacimiento = date_object.strftime('%Y-%m-%d')

        print("Los datos recogidos desde front, MODIFICADOS son: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(vNombreCompleto, vFechaNacimiento, vEmail, vTelefono, vGenero, vOcupacion, vTipoSangre, vPeso, vAltura, vTipoIdentificacion, vNumeroIdentificacion, vDireccionPaciente, vPersonaContacto, vParentescoPaciente, vTelefonoFamiliar, vEnfermedadesCronicas, vAlergias, vAntecedentesFamiliares, vDatosMedicos))

        #Objeto "cs" de tipo cursor, se va a declarar
        cs = mysql.connection.cursor()
        
        #generar query para db_clinica_S181.tb_persona
        vQuery = "INSERT INTO {}.tb_persona (nombre_completo, email, ocupacion, tipo_de_sangre, id_genero) VALUES(\'{}\',\'{}\',\'{}\',\'{}\',{})".format(esquema, vNombreCompleto, vEmail, vOcupacion, vTipoSangre, vGenero)
        print("El query generado es: {}".format(vQuery))
        cs.execute(vQuery)

        #generar query para db_clinica_S181.tb_paciente
        # Consulta SQL para obtener el máximo de la columna id_persona
        vQuery = "SELECT MAX(id_persona) FROM {}.tb_persona".format(esquema)
        print("El query generado es: {}".format(vQuery))
        cs.execute(vQuery)

        # Obtiene el primer elemento de la tupla, que es el valor máximo de la columna id_persona
        idPersona = cs.fetchone()[0]
        print(idPersona)

        vQuery = "INSERT INTO {}.tb_paciente (fecha_nacimiento,enfermedades_cronicas,alergias,antecedentes_familiares,id_persona) VALUES(\'{}\',\'{}\',\'{}\',\'{}\',{})".format(esquema, vFechaNacimiento, vEnfermedadesCronicas, vAlergias, vAntecedentesFamiliares,idPersona)
        print("El query generado es: {}".format(vQuery))
        cs.execute(vQuery)
        #Le decimos a mySQL que queremos hacer una confirmación del cambio
        # al menos debe haber un commit
        mysql.connection.commit()

    #se ocupará para que se pueda mandar el mensaje que informa al usuario que quedó guardado.
    #se utiliza session.pop('_flashes', None) para borrar los mensajes enviados previamente con flash, esto dado que se guardan en la session
    session.pop('_flashes', None)
    flash('El registro fue existoso.')
    cs.close()
    #se ocupará para que, una vez que guardemos, nos regrese al formulario... "registrarPaciente" es el nombre del método
    return redirect(url_for('registrarPaciente'))

##Empieza registro medicos
@app.route('/admon-medicos-registrar', methods=['POST'])
def registrarMedico():
    if request.method == 'POST':

        #Pasamos a variables el contenido de los input, les ponemos una "v" de variable
        vNombreCompleto = request.form['txtNombreCompleto']
        vRFC = request.form['txtRFC']
        vCedula = request.form['txtCedula']
        vEmail = request.form['txtEmail']
        vPassword = request.form['txtPassword']
        vRol = request.form['txtRol']
      
        print("Los datos recogidos desde front son : {}, {}, {}, {}, {}, {}".format(vNombreCompleto, vRFC, vCedula, vEmail, vPassword, vRol))
        
        
        if vRol in ['Administrador','Adminis','Admin','Administrator', 'Admon', 'administrador',' adminis', 'administrador','admin', 'administrator', 'ADMINISTRADOR', 'ADMON', 'ADMINIS', 'ADMIN','ADMINISTRATOR']:
            vRol = 1
        else: 
            vRol = 2

            
        print("Los datos recogidos desde front, MODIFICADOS son: {}, {}, {}, {}, {}, {}".format(vNombreCompleto, vRFC, vCedula, vEmail, vPassword, vRol))

        #Objeto "cs" de tipo cursor, se va a declarar
        cs = mysql.connection.cursor()

        #generar query para db_clinica_S181.tb_persona
        vQuery = "INSERT INTO {}.tb_medicos (Nombre_medico, RFC, cedula_profesional, email, password, id_rol) VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(esquema, vNombreCompleto, vRFC, vCedula, vEmail, vPassword, vRol)
        print("El query generado es: {}".format(vQuery))
        cs.execute(vQuery)

        
        mysql.connection.commit()

    #se ocupará para que se pueda mandar el mensaje que informa al usuario que quedó guardado.
    #se utiliza session.pop('_flashes', None) para borrar los mensajes enviados previamente con flash, esto dado que se guardan en la session
    session.pop('_flashes', None)
    flash('El registro fue existoso.')
    # cs.close()
    #se ocupará para que una vez que guardemos nos regrese al formulario", registrarPaciente es el nombre del método
    return redirect(url_for('registrarMedico'))


##Termina registro medicos

@app.route("/mostrar-registros")
def mostrar():
    cs = mysql.connection.cursor() 
#    cs.execute('SELECT * FROM tbalbums')
    cs.execute("SELECT id, Titulo, Anio FROM tbalbums WHERE Artista LIKE 'Bon%'")
#    for (id, Titulo, Artista, Anio) in cs:
#        print("{}, {}, {} was published on {}".format(id, Titulo, Artista, Anio))

#    for (id, Titulo, Anio) in cs:
#        print("{}, {}, {}".format(id, Titulo, Anio))

    rows = cs.fetchall()

    cs.close()
    return render_template("mostrar-registros.html", albumesRecords = rows)

@app.route('/eliminar')
def eliminar():
    return "se eliminó en la BD "

#Ejecución del servidor en el puerto 5000 
if __name__ =='__main__':
    #app.run(port=5000)
    app.run(port=5000, debug = True)