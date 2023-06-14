#todo lo relacionado con del servidor va aquí

#importación del framework
from flask import Flask
from flask_mysqldb import MySQL

#inicialización del APP (servidor)
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
mysql = MySQL(app)

#Declaración de la inicialización de las rutas. Ésta le pertenece a http://localhost:5000
#Ruta index es la ruta principal
@app.route('/')
def index():
    return "Hola mundo Flask"

@app.route('/guardar')
def guardar():
    return "se guardó en la BD "

@app.route('/eliminar')
def eliminar():
    return "se eliminó en la BD "

#Ejecución del servidor en el puerto 5000 
if __name__ =='__main__':
    app.run(port=5000)
    #app.run(port=5000, debug = True)