from flask_jwt_extended import JWTManager

jwt = JWTManager()

def init_jwt(app):
    from .config import JWT_SECRET_KEY, JWT_ACCESS_TOKEN_EXPIRES

    app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = JWT_ACCESS_TOKEN_EXPIRES

    jwt.init_app(app)
