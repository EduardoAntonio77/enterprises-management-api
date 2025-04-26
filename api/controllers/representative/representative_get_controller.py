from models.representative_model import Representative;

def get_representatives():
    representatives = Representative.query.filter(Representative.delete_at.is_(None)).all()
    return [
        {
            'id': rep.id,
            'name': rep.name
        } for rep in representatives
    ]
