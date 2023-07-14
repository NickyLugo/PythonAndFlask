#Examen 2do parcial

from flask import Flask, render_template, request, redirect, url_for, flash

from flask_mysqldb import MySQL

#inicialización del APP (servidor)
app=Flask(__name__)

# configuración de la conexión a base de datos.
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root' 

app.config['MYSQL_PASSWORD']=''

app.config['MYSQL_DB']='db_floreria'

app.secret_key='mysecretkey'
mysql = MySQL(app)

#Ruta principal Index
@app.route('/')
def index():

    #Cursor de la consulta cc
    cc = mysql.connection.cursor()
    cc.execute('select * from tbflores')
    #El resultado de la consulta lo guardamos en una variable que se llame conAlbums
    conFlores = cc.fetchall()
    #print(conFlores)
    return render_template('index.html', floresStock = conFlores)

#Ruta para guardar
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':

        #Pasamos a variables el contenido de los input, les ponemos una "V" de variable
        Vflor = request.form['txtFlor']
        Vstock = request.form['txtStock']
        Vprecio = request.form['txtPrecio']
        print (Vflor, Vstock, Vprecio)
        
        #Objeto "CS" de tipo cursor, se va a declarar
        CS = mysql.connection.cursor() 
        #dos parametros el primero es el insert de los datos y el segundo parametro son las variables
        CS.execute('insert into tbflores(flor, stock, precio) values(%s, %s, %s)',(Vflor, Vstock, Vprecio))

        #Le decimos a mySQL que queremos hacer una confirmación del cambio
        mysql.connection.commit()

    """ return "se guardó en la BD " """
    '''return 'los datos llegaron amigo ;)'''

    #se ocupará para que se pueda mandar el mensaje que informa al usuario que quedó guardado.
    flash('El registro de flor fue agregado correctamente amigo')
    #se ocupará para que una vez que guardemos nos regrese al formulario
    return redirect(url_for('index'))

    #Código Jinja {% %}

@app.route("/mostrar-registros")
def mostrar():
    cs = mysql.connection.cursor() 
#    cs.execute('SELECT * FROM tbflores')
    cs.execute("SELECT id, flor, stock, precio FROM tbflores WHERE flor LIKE 'Ros%'")
#    for (id, Flor, Cantidad, Precio) in cs:
#        print("{}, {}, {} was published on {}".format(id, Titulo, Artista, Anio))

    rows = cs.fetchall()

    cs.close()
    return render_template("mostrar-registros.html", floresStock = rows)

""" si no viene el parametro, no va a encontrar la flor """
@app.route('/editar/<id>')
def editar(id):
        cursoID = mysql.connection.cursor()
        """ cursoID.execute('SELECT * FROM tbflores WHERE id= %s', (id,)) """
        """ id, nos ayuda a detectar  """ 
        cursoID.execute('SELECT * FROM tbflores WHERE id= %s', (id))
        """ consultaId = cursoID.fetchall() """
        consultaId = cursoID.fetchone()
        return render_template('editarFlor.html', flor = consultaId)

@app.route('/actualizar/<id>', methods =["POST"])
def actualizar(id):
    if request.method == 'POST':
        
         #Pasamos a variables el contenido de los input, les ponemos una "var" de variable
        varFlor = request.form['txtFlor']
        varStock = request.form['txtStock']
        varPrecio = request.form['txtPrecio']

        print(varFlor, varStock, varPrecio)

        #Objeto "curAct" de tipo cursor, se va a declarar
        curAct = mysql.connection.cursor() 
        
        #dos parametros el primero es el insert de los datos y el segundo parametro son las variables
        curAct.execute('UPDATE tbflores set flor = %s, stock = %s, precio = %s WHERE id = %s', (varFlor, varStock, varPrecio, id))

        #Le decimos a mySQL que queremos hacer una confirmación del cambio
        mysql.connection.commit()
        #se ocupará para que se pueda mandar el mensaje que informa al usuario que quedó guardado.

    flash('El registro de la nueva flor se actualizó correctamente amigo'+' '+'flor: '+varFlor)
    #se ocupará para que una vez que guardemos nos regrese al formulario
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
        cursoID = mysql.connection.cursor()
        """ cursoID.execute('SELECT * FROM tbflores WHERE id= %s', (id,)) """
        """ id, nos ayuda a detectar el registro correcto a eliminar """ 
        cursoID.execute('SELECT * FROM tbflores WHERE id= %s', (id))
        """ consultaId = cursoID.fetchall() """
        consultaId = cursoID.fetchone()
        return render_template('eliminarFlor.html', flor = consultaId)

@app.route('/eliminar/<id>', methods =["POST"])
def eliminar(id):
    if request.method == 'POST':
        
        varTitulo = request.form['txtFlor']
        #Objeto "CS" de tipo cursor, se va a declarar
        curDel = mysql.connection.cursor() 
        
        #dos parametros el primero es el insert de los datos y el segundo parametro son las variables
        curDel.execute('DELETE from tbflores WHERE id = %s', (id,))

        #Le decimos a mySQL que queremos hacer una confirmación del cambio
        mysql.connection.commit()
        #se ocupará para que se pueda mandar el mensaje que informa al usuario que quedó guardado.

    flash('El album fue eliminado correctamente amig@'+' '+'título: '+varTitulo)
    #se ocupará para que una vez que guardemos nos regrese al formulario
    return redirect(url_for('index'))

@app.route('/Consulta-por-nombre')
def consultaPorNombre():
    consultaCursor= mysql.connection.cursor()
    consultaCursor.execute('select * from tbflores')
    confruta= consultaCursor.fetchall()
    print(confruta)
    return render_template('consulta-por-nombre.html', listafruta = confruta)

@app.route('/ChecarFruta')
def Consult():
    return render_template('consultando.html')

@app.route('/Consultandolo', methods=['POST'])
def consultanombre():
    Varbuscar= request.form['txtbuscar']
    print(Varbuscar)
    CC= mysql.connection.cursor()
    CC.execute('select * from tbfrutas where fruta LIKE %s', (f'%{Varbuscar}%',))
    confruta= CC.fetchall()
    print(confruta)
    return render_template('consultando.html', listafruta = confruta)

#Ejecución del servidor en el puerto 5000 
if __name__ =='__main__':
    app.run(port=5000)
    #app.run(port=5000, debug = True)