import pymysql
pymysql.install_as_MySQLdb()

from app import App
from waitress import serve

# Cria uma instância da aplicação
app_instance = App()
flask_app = app_instance.app
flask_app.config['DEBUG'] = True

# Para rodar localmente com `python server.py`
if __name__ == "__main__":
    serve(flask_app, host="0.0.0.0", port=5000)