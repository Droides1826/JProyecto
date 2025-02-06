from flask import Flask 
from flask_cors import CORS
from utils.db import conexion
from routes.productos import productos
from routes.categorias import categorias
from routes.pedidos import pedidos

app = Flask(__name__, template_folder='template')
CORS(app, resources={r"/": {"origins": "", "methods": ["GET", "POST", "PUT", "DELETE"], "allow_headers": ["Content-Type", "Authorization"]}})
#conexion a la base de datoss
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pproyecto'
conexion.init_app(app)

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'jfif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(productos)
app.register_blueprint(categorias)
app.register_blueprint(pedidos)
