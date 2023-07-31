#todo lo relacionado con del servidor va aquí

#importación del framework
from flask import Flask, render_template, request, redirect, url_for, flash
#flash se ocupa para poder ...
from flask_mysqldb import MySQL

#inicialización del APP (servidor)
app=Flask(__name__)

# configuración de la conexión a base de datos.
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root' 
#Laptop
app.config['MYSQL_PASSWORD']=''
#Desktop
#app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='dbflask'
#Se agrega para evitar RuntimeError: The session is unavailable because no secret key was set.
app.secret_key='mysecretkey'
mysql = MySQL(app)
# si es posible conectarse a dos bases de datos

#Declaración de la inicialización de las rutas. Ésta le pertenece a http://localhost:5000
#Ruta index es la ruta principal
#El archivo principal de las interfaces debe tener el 'index'
@app.route('/')
def index():
    #return "Hola mundo Flask"
    #Cursor de la consulta cc
    cc = mysql.connection.cursor()
    cc.execute('select * from tbalbums')
    #El resultado de la consulta lo guardamos en una variable que se llame conAlbums
    conAlbums = cc.fetchall()
    #print(conAlbums)
    return render_template('index.html', albumesRecords = conAlbums)

'''
@app.route('/otra')
def index2():
    #return "Hola mundo Flask"
    return render_template('index.html')

'''
#Método de trabajo POST que trabaja por detrás de lo que ve el usuario
#Recibe un envío de un formulario RUTA http:localhost:5000/ guardar tipo POST para insert
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':

        #Pasamos a variables el contenido de los input, les ponemos una "V" de variable
        Vtitulo = request.form['txtTitulo']
        Vartista = request.form['txtArtista']
        Vanio = request.form['txtAnio']
        print (Vtitulo, Vartista, Vanio)
        
        #Objeto "CS" de tipo cursor, se va a declarar
        CS = mysql.connection.cursor() 
        #dos parametros el primero es el insert de los datos y el segundo parametro son las variables
        CS.execute('insert into tbalbums(titulo, artista, anio) values(%s, %s, %s)',(Vtitulo, Vartista, Vanio))

        #Le decimos a mySQL que queremos hacer una confirmación del cambio
        mysql.connection.commit()

    """ return "se guardó en la BD " """
    '''return 'los datos llegaron amigo ;)'''

    #se ocupará para que se pueda mandar el mensaje que informa al usuario que quedó guardado.
    flash('El album fue agregado correctamente amig@')
    #se ocupará para que una vez que guardemos nos regrese al formulario
    return redirect(url_for('index'))

    #Código Jinja {% %}

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

""" si no viene el parametro, no va a encontrar la ruta """
@app.route('/editar/<id>')
def editar(id):
        cursoID = mysql.connection.cursor()
        """ cursoID.execute('SELECT * FROM tbalbums WHERE id= %s', (id,)) """
        """ id, nos ayuda a detectar  """ 
        cursoID.execute('SELECT * FROM tbalbums WHERE id= %s', (id))
        """ consultaId = cursoID.fetchall() """
        consultaId = cursoID.fetchone()
        return render_template('editarAlbum.html', album = consultaId)

@app.route('/actualizar/<id>', methods =["POST"])
def actualizar(id):
    if request.method == 'POST':
        
         #Pasamos a variables el contenido de los input, les ponemos una "var" de variable
        varTitulo = request.form['txtTitulo']
        varArtista = request.form['txtArtista']
        varAnio = request.form['txtAnio']
        print(varTitulo, varArtista, varAnio)

        #Objeto "curAct" de tipo cursor, se va a declarar
        curAct = mysql.connection.cursor() 
        
        #dos parametros el primero es el insert de los datos y el segundo parametro son las variables
        curAct.execute('UPDATE tbalbums set titulo = %s, artista = %s, anio = %s WHERE id = %s', (varTitulo, varArtista, varAnio, id))

        #Le decimos a mySQL que queremos hacer una confirmación del cambio
        mysql.connection.commit()
        #se ocupará para que se pueda mandar el mensaje que informa al usuario que quedó guardado.

    flash('El album fue actualizado correctamente amig@'+' '+'título: '+varTitulo)
    #se ocupará para que una vez que guardemos nos regrese al formulario
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
        cursoID = mysql.connection.cursor()
        """ cursoID.execute('SELECT * FROM tbalbums WHERE id= %s', (id,)) """
        """ id, nos ayuda a detectar el registro correcto a eliminar """ 
        cursoID.execute('SELECT * FROM tbalbums WHERE id= %s', (id))
        """ consultaId = cursoID.fetchall() """
        consultaId = cursoID.fetchone()
        return render_template('eliminarAlbum.html', album = consultaId)

@app.route('/eliminar/<id>', methods =["POST"])
def eliminar(id):
    if request.method == 'POST':
        
        varTitulo = request.form['txtTitulo']
        #Objeto "CS" de tipo cursor, se va a declarar
        curDel = mysql.connection.cursor() 
        
        #dos parametros el primero es el insert de los datos y el segundo parametro son las variables
        curDel.execute('DELETE from tbalbums WHERE id = %s', (id,))

        #Le decimos a mySQL que queremos hacer una confirmación del cambio
        mysql.connection.commit()
        #se ocupará para que se pueda mandar el mensaje que informa al usuario que quedó guardado.

    flash('El album fue eliminado correctamente amig@'+' '+'título: '+varTitulo)
    #se ocupará para que una vez que guardemos nos regrese al formulario
    return redirect(url_for('index'))

#Ejecución del servidor en el puerto 5000 
if __name__ =='__main__':
    app.run(port=5000)
    #app.run(port=5000, debug = True)