# imports
from flask import Flask;
from flask_cors import CORS;
from flask_migrate import Migrate;
from database import database;

from routes import register_routes;

# essential config
app = Flask(__name__);

CORS(app, origins='http://localhost:3000');

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:2905@localhost:3306/enterpriseapi';
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;

database.init_app(app);
migrate = Migrate(app, database);

# registering blueprints
register_routes(app);

# app will only init on main file "app.py"
if __name__ == '__main__':
    app.run(debug=True);
