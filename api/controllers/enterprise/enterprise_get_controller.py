from models.enterprise_model import Enterprise

def get_enterprises():
    enterprises = Enterprise.query.filter(Enterprise.delete_at.is_(None)).all()
    return [
        {
            'id': rep.id,
            'name': rep.name,
            'representative_id': rep.representative_id
        } for rep in enterprises
    ]
