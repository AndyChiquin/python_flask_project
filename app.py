from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, this is a Flask project running on a web server!'

if __name__ == '__main__':
    # Usar el puerto proporcionado por Railway o el 5000 por defecto
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
