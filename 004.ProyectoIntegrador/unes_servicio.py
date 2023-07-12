#todo lo relacionado con del servidor va aquí

#importación del framework
from flask import Flask, render_template, request, redirect, url_for, flash, session
#flash se ocupa para poder crear mensajes de respuesta con ayuda de JINJA motor de plantillas
#Se importa para desmenuzar la fecha 
from flask_mysqldb import MySQL
#Se importa para desmenuzar la fecha 
from datetime import datetime

#inicialización del APP (servidor)
app=Flask(__name__)

# configuración de la conexión a base de datos.
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root' 
#Laptop
app.config['MYSQL_PASSWORD']=''
#Desktop
#app.config['MYSQL_PASSWORD']='root'

app.config['MYSQL_DB']='db_unes_s181'
esquema = 'db_unes_s181'

#Se agrega para evitar RuntimeError: The session is unavailable because no secret key was set.
app.secret_key='mysecretkey'
mysql = MySQL(app)

# si es posible conectarse a dos bases de datos
# mas que nada cuando se realizan migraciones; conciliaciones de cuentas;
# de contratos; conciliación de facturas, de pagos. En especial en sistemas distribuidos. 

#Declaración de la inicialización de las rutas. Ésta le pertenece a http://localhost:5000
#Ruta '/' es la ruta principal

#El archivo principal de las interfaces debe tener el 'index'

@app.route('/')
def iniciarLoginUnes():
    return render_template('a-login-unes.html')

@app.route('/registro-personas-unes')
def iniciarRegistroPersonaUnes():
    return render_template('b-registro-persona.html')

@app.route('/botones-chofer-o-pasajero')
def iniciarChoferOPasajeroUnes():
    return render_template('c-botones-chofer-o-pasajero.html')

@app.route('/pantalla-principal')
def iniciarPantallaPrincipalUnes():
    return render_template('d-pantalla-principal.html')

@app.route('/buscar-viaje')
def iniciarBuscarViajeUnes():
    return render_template('e-buscar-viaje.html')

@app.route('/registro-vehiculo-unes')
def iniciarRegistroVehiculoUnes():
    return render_template('f-registro-vehiculo.html')

@app.route('/publicar-viaje')
def iniciarPublicarViajeUnes():
    return render_template('g-publicar-viaje.html')

@app.route('/mi-perfil')
def iniciarMiPerfil():
    return render_template('h-perfil-usuario.html')


'''
@app.route('/', methods=['POST'])
def LoginUnes():
    if request.method == 'POST':

        #Pasamos a variables el contenido de los input, les ponemos una "v" de variable
        vUser = request.form["txtUser"]
        vPassword = request.form['txtContrasena']
        
        print("Los datos recogidos desde front son : {}, {}".format(vUser, vPassword))

        #Objeto "cs" de tipo cursor, se va a declarar
        cs = mysql.connection.cursor()
        
        #cs.execute('INSERT INTO tb_login(nombre_usuario, contrasena) values(%s, %s)',(vUser, vPassword))

        #generar query para db_unes_s181.tb_login
        vQuery = "INSERT INTO {}.tb_login (nombre_usuario, contrasena) VALUES(\'{}\',\'{}\')".format(esquema, vUser, vPassword)
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
    #se ocupará para que una vez que guardemos nos regrese al formulario", registrarPaciente es el nombre del método
    return redirect(url_for('iniciarLoginUnes'))
    '''


#Método de trabajo POST que trabaja por detrás de lo que ve el usuario
@app.route('/registro-personas-unes', methods=['POST'])
def registrarPersona():
    if request.method == 'POST':

        #Pasamos a variables el contenido de los input, les ponemos una "v" de variable
        vNombrePersona = request.form["txtNombrePersona"]
        vApellidoPaternoPersona = request.form['txtApellidoPaterno']
        vApellidoMaternoPersona = request.form['txtApellidoMaterno']
        vFechaNacimiento = request.form['dateFechaNacimiento']
        vCarrera = request.form['txtCarrera']
        vEmail = request.form['txtEmail']
        vTelefono = request.form['numberTelefono']   


        
        print("Los datos recogidos desde front son : {}, {}, {}, {}, {}, {}".format(vNombrePersona, vApellidoPaternoPersona, vApellidoMaternoPersona, vFechaNacimiento, vCarrera, vEmail, vTelefono))
        
        vFechaNacimiento = request.form['dateFechaNacimiento']
        date_object = datetime.strptime(vFechaNacimiento, '%Y-%m-%d')
        vFechaNacimiento = date_object.strftime('%Y-%m-%d')

        # Save the formatted_date to MySQL
        # Example MySQL code:
        # cursor.execute("INSERT INTO your_table (date_column) VALUES (%s)", (formatted_date,))
        # connection.commit()

        print("Los datos recogidos MODIFICADOS son: {}, {}, {}, {}, {}, {}, {}".format(vNombrePersona, vApellidoPaternoPersona, vApellidoMaternoPersona, vFechaNacimiento, vCarrera, vEmail, vTelefono))

        #Objeto "cs" de tipo cursor, se va a declarar
        cs = mysql.connection.cursor()
        
        #cs.execute('INSERT INTO tb_persona(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, carrera, email, telefono) values(%s, %s, %s, %s, %s, %s, %s)',(vNombrePersona, vApellidoPaternoPersona, vApellidoMaternoPersona, vFechaNacimiento, vCarrera, vEmail, vTelefono))

            #generar query para db_clinica_S181.tb_persona
        vQuery = "INSERT INTO {}.tb_persona (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, carrera, email, telefono) VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(esquema, vNombrePersona, vApellidoPaternoPersona, vApellidoMaternoPersona, vFechaNacimiento, vCarrera, vEmail, vTelefono)
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
    #se ocupará para que una vez que guardemos nos regrese al formulario", registrarPaciente es el nombre del método
    """ return redirect(url_for('registrarPersona')) """
    return redirect(url_for('iniciarLoginUnes'))

@app.route('/pantalla-principal', methods=['POST'])
def elegirDesdeMain():
    """ if request.method == 'POST': """

    return redirect(url_for('iniciarLoginUnes'))

#Ejecución del servidor en el puerto 5000 
if __name__ =='__main__':
    app.run(port=5000)
    #app.run(port=5000, debug = True)