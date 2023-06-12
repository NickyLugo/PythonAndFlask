# Todo lo relacionado con el servidor
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
        return "Hola Mundo Flask"

if __name__ == '__main__':
        app.run(port=5000)