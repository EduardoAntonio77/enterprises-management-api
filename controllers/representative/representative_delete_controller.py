from database import database;
from models.representative_model import Representative;
from datetime import timezone, datetime;

def delete_representative_controller(repre_id):
    repre = Representative.query.get(repre_id);

    repre.delete_at = datetime.now(timezone.utc); # Caso não aconteça nenhum dos erros acima, preenchera o campo "deleted_at" do id passado com o horario atual.
    
    repre.deleted_at = datetime.now(timezone.utc);
    database.session.commit();
    return repre;
