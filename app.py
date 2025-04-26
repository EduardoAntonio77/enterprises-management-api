# imports
from flask import Flask;
from flask_cors import CORS;
from flask_migrate import Migrate;

from config.database import database;
from routes import register_routes;

from flask_jwt_extended import JWTManager
from config.jwt_utils.manager import init_jwt

# Classe que sera responsavel pela criação, configuração e execução da aplicação
class App:

    # Uma função que recebe como metodo "__init__"  que por sua vez é executado automaticamente para criar a aplicação e configurar tudo que esta dentro do __init__.   
    def __init__(self):
        self.app = Flask(__name__)

        # Chama um metodo da classe para configurar variáveis da aplicação.
        self.configure_app()

        # Chama um metodo da classe para inicializar as extensções do Flask como: CORS, Migreate e JWT.
        self.configure_extensions()

        # Chama a função responsavel pela adição das rotas ao app
        self.register_routes()

    def configure_app(self):

        # Define a URL ou caminho de conexão ao banco de dados MySQL
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:2905@localhost:3306/enterpriseapi'
        
        # Desativa uma opção do SQLAlchemy que monitora em tempo real modificações no projeto (è ativada por padrão porem, para econimia de recursos é melhor desativa-la).
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    def configure_extensions(self):

        # Ativa o CORS permitindo requisições do frontend.
        CORS(self.app, origins='http://localhost:3000')

        # Inicializa o SQLAlchemy com a app (lembrando que "database" é um objeto importatdo de outro arquivo onde database recebe as funcionalidades do SQLAlchemy).
        database.init_app(self.app)

        # Configura o Flask-Migrate com o app e objeto do banco.
        Migrate(self.app, database)

        # Configurações do JWT como secret key, tempo de expiração do token entre outros
        init_jwt(self.app)

        # Inicializa o gerenciador de JWT (permitindo que o @jwt_required possa ser usado nas rotas)
        JWTManager(self.app)

    # Chama a função responsavel por registrar todos os blueprints das rotas da aplicação.
    def register_routes(self):
        register_routes(self.app)

    # Iniciara o servidor flask
    def run(self, **kwargs):
        self.app.run(**kwargs)

# Nota para nao esquecer: O self nos argumentos de cada função serve como referencia a instancia atual da classe. Quando chamado nos argumentos, basicamente esta acessando o nonme da propria instancia.