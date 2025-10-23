import uuid
from .database_service import users_db

def add_user(user_data):
    user_id = str(uuid.uuid4())
    data = {"id": user_id, **user_data}
    users_db.insert(data)
    return data

def get_all_users():
    return users_db.all()

def get_user_by_id(user_id):
    results = users_db.search(lambda u: u["id"] == user_id)
    return results[0] if results else None
