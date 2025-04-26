from api.flask import App
import os

# Cria uma instância da aplicação
app_instance = App()
flask_app = app_instance.app

# Função que o Vercel vai chamar
def handler(environ, start_response):
    return flask_app(environ, start_response)

# Para rodar localmente com `python server.py`
if __name__ == "__main__":
    app_instance.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
