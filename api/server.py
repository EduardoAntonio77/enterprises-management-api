from app import App
from waitress import serve

# Cria uma instância da aplicação
app_instance = App()
flask_app = app_instance.app

# Para rodar localmente com `python server.py`
if __name__ == "__main__":
    # Usando Waitress para rodar o app Flask
    serve(flask_app, host="0.0.0.0", port=5000)
