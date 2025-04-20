from models.representative_model import Representative
from flask import g
from config.jwt_utils.tokens import generate_access_token

def representative_login():
    rep = g.representative

    token = generate_access_token({
        "id": rep.id,
        "email": rep.email
    })

    return {
        "access_token": token
    }