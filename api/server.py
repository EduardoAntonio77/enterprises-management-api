import pymysql
pymysql.install_as_MySQLdb()

from app import App
from waitress import serve
from dotenv import load_dotenv
import os

load_dotenv()

# Cria uma instância da aplicação
app_instance = App()
flask_app = app_instance.app
flask_app.config['DEBUG'] = True
port_dotenv = os.environ.get("PORT")

if __name__ == "__main__":    
    print(f"API running in: http://127.0.0.1:{port_dotenv}")
    print("API Documentation running in: http://localhost:5000/apidocs")
    # flask_app.run(ssl_context='adhoc', debug=True)
    flask_app.run(host="127.0.0.1", port=5000, debug=True)
