import datetime
from flask_jwt_extended import create_access_token

def generate_access_token(data):
    expiration = datetime.timedelta(hours=1) 
    return create_access_token(identity=str(data['id']), expires_delta=expiration)
