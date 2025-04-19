from models.representative_model import Representative

def authenticate_user(email, password):
    rep = Representative.query.filter_by(email=email, delete_at=None).first()
    if rep and rep.password == password:
        return rep
    return None
