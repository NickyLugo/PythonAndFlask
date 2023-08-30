
#importación del framework
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin

#Se importa para desmenuzar la fecha 
from flask_mysqldb import MySQL

#Se importa para desmenuzar la fecha
from datetime import datetime
#from flask_login import UserMixin
#from flask_login import LoginManager

login_manager = LoginManager()

from flask import Flask
import pyodbc

#inicialización del APP (servidor)
app = Flask(__name__)
#login_manager.init_app(app)
app.secret_key='mysecretkey'


class User(UserMixin):
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password
        # Other user attributes here

    def get_id(self):
        return str(self.id)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, inicia sesión para acceder a esta página.' 

@login_manager.user_loader
def load_user(id):
    print("este es mi id: " + id)
    cursor = connection.cursor()
    cursor.execute('SELECT id_Persona, email, contrasena FROM tb_personas WHERE id_Persona = ?', (id))
    persona = cursor.fetchone()
    if persona:
        print("Metodo: load_user(id), el usuario si coincide.")
        #return User(id='1', email='121038198@upq.edu.mx', password='123')
        return User(id=persona[0], email=persona[1], password=persona[2])
    return None

try:
    app.config['SQL_SERVER_URI'] = 'DRIVER={SQL Server};SERVER=LAPTOP-H5L1Q96Q;DATABASE=db_unes_proyecto'
#UID=dba_NickLugo;PWD=123456
    # Test if the connection is successful
    connection = pyodbc.connect(app.config['SQL_SERVER_URI'])
    print("Conexión exitosa")
except Exception as ex:
    print(ex)

@app.route('/')
def iniciarMenuPublico():
    return render_template('0-menuPublico.html')

@app.route('/acerca-nosotros')
def iniciarNosotros():
    return render_template('0-acercaNosotros.html')

@app.route('/login')
def iniciarLoginUnes():
    return render_template('a-login-unes.html')


@app.route('/login', methods=['POST'])
def login():
  
    if request.method == 'POST':
        vEmail = request.form['txtEmail']
        vPassword = request.form['txtContrasena']

        print("Metodo: login(), email y pass que llegan desde front: email {} pass {}".format(vEmail, vPassword))

        cursor = connection.cursor()
        cursor.execute('SELECT id_Persona, email, contrasena FROM tb_personas WHERE email = ? and contrasena = ?', (vEmail, vPassword))
        persona = cursor.fetchone()

        print("Metodo: login(), antes de validar email y pass")
        if persona:
            print("Metodo: login(), email y pass correctos")
            user = User(id=persona[0], email=persona[1], password=persona[2])
            print()
            login_user(user)
            return redirect(url_for('iniciarChoferOPasajeroUnes'))
        else:
            print("Usuario o Contraseña Incorrectas")
            flash('Usuario o Contraseña Incorrectas')
            return render_template('a-login-unes.html')
    else:
        print("Datos login incompletos")
        return render_template('a-login-unes.html')
    
@app.route('/logout')
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente!')
    return redirect(url_for('iniciarLoginUnes'))

@app.route('/menu')
@login_required
def iniciarMenu():
    return render_template('menu.html')

@app.route('/registro-personas-unes')
def iniciarRegistroPersonaUnes():
    return render_template('b-registro-persona.html')

@app.route('/botones-chofer-o-pasajero')
@login_required
def iniciarChoferOPasajeroUnes():
    return render_template('c-botones-chofer-o-pasajero.html')

@app.route('/pantalla-principal')
@login_required
def iniciarPantallaPrincipalUnes():
    return render_template('d-pantalla-principal.html')

@app.route('/buscar-viaje')
@login_required
def iniciarBuscarViajeUnes():
    return render_template('e-buscar-viaje.html')

@app.route('/registro-vehiculo-unes')
@login_required
def iniciarRegistroVehiculoUnes():
    return render_template('f-registro-vehiculo.html')

@app.route('/mi-perfil')
@login_required
def iniciarMiPerfil():
    return render_template('h-perfil-usuario.html')

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
        vPassword = request.form['txtPassword']
        vTelefono = request.form['numberTelefono']   

        print("Los datos recogidos desde front son : {}, {}, {}, {}, {}, {}, {}".format(vNombrePersona, vApellidoPaternoPersona, vApellidoMaternoPersona, vFechaNacimiento, vCarrera, vEmail, vPassword, vTelefono))
        
        vFechaNacimiento = request.form['dateFechaNacimiento']
        date_object = datetime.strptime(vFechaNacimiento, '%Y-%m-%d')
        vFechaNacimiento = date_object.strftime('%Y-%m-%d')

        print("Los datos recogidos MODIFICADOS son: {}, {}, {}, {}, {}, {}, {}, {}".format(vNombrePersona, vApellidoPaternoPersona, vApellidoMaternoPersona, vFechaNacimiento, vCarrera, vEmail, vPassword, vTelefono))
        
        #QUERY
        consulta =pyodbc.connect(app.config['SQL_SERVER_URI'])
        cursor = consulta.cursor()
        #cursor.execute('EXEC InsertarEnLogin;')
        cursor.execute('INSERT INTO tb_personas(nombre_Usuario, ape_Paterno, ape_Materno, fecha_Nacimiento, carrera, email, contrasena, telefono) VALUES (?,?,?,?,?,?,?,?)',(vNombrePersona, vApellidoPaternoPersona, vApellidoMaternoPersona, vFechaNacimiento, vCarrera, vEmail, vPassword, vTelefono))
        consulta.commit()
        consulta.close()        

    session.pop('_flashes', None)
    flash('El registro fue existoso.')
    #cs.close()
    #se ocupará para que una vez que guardemos nos regrese al formulario", registrarPaciente es el nombre del método
    """ return redirect(url_for('registrarPersona')) """
    return redirect(url_for('iniciarLoginUnes'))

@app.route('/pantalla-principal', methods=['POST'])
@login_required
def elegirDesdeMain():
    print("Entra a metodo elegirDesdeMain()")
    return redirect(url_for('iniciarPantallaPrincipalUnes'))

@app.route('/buscar-viaje', methods=['POST'])
@login_required
def buscarViaje():
    varRuta = request.form['txtRuta']
    cursor = connection.cursor()
    query = "SELECT * FROM tb_Viajes WHERE Ruta LIKE \'%{}%\'".format(varRuta)
    print("query: " + query)
    cursor.execute(query)
    registrosViajes = cursor.fetchall()
    return render_template('e-buscar-viaje.html', viajes=registrosViajes)

@app.route('/viaje')
@login_required
def index():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tb_Viajes')
    registrosViajes = cursor.fetchall()
    return render_template('iii-viajesindex.html', viajes=registrosViajes)

@app.route('/guardar', methods=['POST'])
@login_required
def guardar():
    if request.method == 'POST':
        varRuta = request.form['txtRuta']
        varChofer = request.form['txtChofer']
        varAsientos = request.form['txtAsientos']
        
        cursor = connection.cursor()
        cursor.execute('INSERT INTO tb_Viajes (Ruta, Chofer, Asientos) VALUES (?, ?, ?)', (varRuta, varChofer, varAsientos))
        connection.commit()

        flash('El viaje fue agregado correctamente.')
        return redirect(url_for('index'))

@app.route('/editar/<id>')
@login_required
def editar(id):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tb_Viajes WHERE Id = ?', (id,))
    registroViaje = cursor.fetchone()
    return render_template('i-viajeseditar.html', viaje=registroViaje)

@app.route('/actualizar/<id>', methods=["POST"])
@login_required
def actualizar(id):
    if request.method == 'POST':
        varRuta = request.form['txtRuta']
        varChofer = request.form['txtChofer']
        varAsientos = request.form['txtAsientos']
        
        cursor = connection.cursor()
        cursor.execute('UPDATE tb_Viajes SET Ruta = ?, Chofer = ?, Asientos = ? WHERE Id = ?', (varRuta, varChofer, varAsientos, id))
        connection.commit()

        flash('El viaje fue actualizado correctamente.')
        return redirect(url_for('index'))

@app.route('/delete/<id>')
@login_required
def delete(id):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tb_Viajes WHERE Id = ?', (id,))
    registroViaje = cursor.fetchone()
    return render_template('ii-viajeseliminar.html', viaje=registroViaje)

@app.route('/eliminar/<id>', methods=["POST"])
@login_required
def eliminar(id):
    if request.method == 'POST':
        cursor = connection.cursor()
        cursor.execute('DELETE FROM tb_Viajes WHERE Id = ?', (id,))
        connection.commit()

        flash('El viaje fue eliminado correctamente.')
        return redirect(url_for('index'))

import pdfkit
import jinja2
from flask import send_file
from datetime import datetime

@app.route('/download-report-pdf', methods=['GET'])
def download_pdf():
    
    #conn: None
    #cursor: None

    try:
        #conn: mysql.connect()
        #cursor = conn.cursor(pymysql.cursors.DictCursor)
          
        NombrePaciente = "Nick"
        Edad="1"
        FechaHoy = datetime.today().strftime("%d %b, %Y")
        Peso = "80 kg"
        Altura = "1.75"
        Temperatura = "28"
        Ritmo = "65"
        Glucosa = "200"
        Diagnostico = "Tiene Diabetes"
        Tratamiento = "Tomar 1 Dulcolax c/24 horas durante 3 días"
        NombreMedico = "Alan"
        Cedula = "12345"

        context = {'txtNombrePaciente': NombrePaciente,'txtEdad': Edad, 'txtFecha': FechaHoy, 'txtPeso': Peso, 'txtAltura': Altura, 'txtTemperatura': Temperatura, 'txtRitmo': Ritmo, 'txtGlucosa': Glucosa, 'txtDiagnostico': Diagnostico, 'txtTratamiento': Tratamiento, 'txtNombreMedico': NombreMedico, 'txtCedulaMedico': Cedula}

        template_loader = jinja2.FileSystemLoader('receta.html')
        template_env = jinja2.Environment(loader=template_loader)

        html_template= r'C:\Users\nicky\Documents\GitHub\Flask_S181\004.ProyectoIntegrador\templates\receta.html'
        template = template_env.get_template(html_template)
        output_text = template.render(context)

        print("HTML Template Path:", html_template)
        print("CSS Path:")
        #print("wkhtmltopdf Path:", config.wkhtmltopdf)
        print("wkhtmltopdf Path:", config.configuration['wkhtmltopdf'])

        config = pdfkit.configuration(wkhtmltopdf = 'C:\Program Files\wkhtmltopdf')
        
        #output_pdf = 'C:\Users\nicky\Documents\GitHub\Flask_S181/pdf_generado.pdf'
        output_pdf = r'C:\Users\nicky\Documents\GitHub\Flask_S181\pdf_generado.pdf'

        pdfkit.from_string(output_text, output_pdf, configuration=config) #css=''
        #return send_file(output_pdf, as_attachment=True)
        print("Template Output:")
        print(output_text)
        

    except Exception as e:
        print("An error occurred:", e)
        return "An error occurred while generating the PDF."

    # Return the PDF file if everything is successful
    print("PDF Generated Successfully:", output_pdf)
    return send_file(output_pdf, as_attachment=True)
''' finally:
            cursor.close()
            conn.close() '''


#Ejecución del servidor en el puerto 5000 
if __name__ =='__main__':
    #app.run(port=5001)
    app.run(port=5000, debug = True)