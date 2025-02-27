# Inicializa o aplicativo Flask e importa as rotas
from flask import Flask

# Inicializando o aplicativo Flask
app = Flask(__name__)

# Importar rotas para evitar importações circulares
from app import routes
