from app import App
import os

# Cria uma instância da aplicação
app_instance = App()
flask_app = app_instance.app

# Para rodar localmente com `python server.py`
if __name__ == "__main__":
    app_instance.run(debug=True)
