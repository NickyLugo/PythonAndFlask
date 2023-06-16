#todo lo relacionado con del servidor va aquí

#importación del framework
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

#inicialización del APP (servidor)
app=Flask(__name__)

# configuración de la conexión a base de datos.
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
mysql = MySQL(app)
# si es posible conectarse a dos bases de datos

#Declaración de la inicialización de las rutas. Ésta le pertenece a http://localhost:5000
#Ruta index es la ruta principal
#El archivo principal de las interfaces debe tener el 'index'
@app.route('/')
def index():
    #return "Hola mundo Flask"
    return render_template('index.html')

#Método de trabajo POST que trabaja por detrás de lo que ve el usuario
#Recibe un envío de un formulario RUTA http:localhost:5000/ guardar tipo POST para insert
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        artista = request.form['txtArtista']
        anio = request.form['txtAnio']
        print (titulo, artista, anio)
        
    """ return "se guardó en la BD " """
    return 'los datos llegaron amigo ;)'

@app.route('/eliminar')
def eliminar():
    return "se eliminó en la BD "

#Ejecución del servidor en el puerto 5000 
if __name__ =='__main__':
    app.run(port=5000)
    #app.run(port=5000, debug = True)