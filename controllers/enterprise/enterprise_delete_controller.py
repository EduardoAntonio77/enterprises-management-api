from config.database import database;
from models.enterprise_model import Enterprise;
from datetime import datetime, timezone;

def enterprise_delete_controller(id):
    enterprise = Enterprise.query.get(id);

    enterprise.deleted_at = datetime.now(timezone.utc);

    database.session.commit();
    return enterprise;
