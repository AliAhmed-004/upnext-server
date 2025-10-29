import uuid
from .database_service import users_table 

def add_user(user_data):
    user_id = str(uuid.uuid4())
    data = {"id": user_id, **user_data}
    users_table.insert(data)
    return data

def get_all_users():
    return users_table.all()

def get_user_by_id(user_id):
    results = users_table.search(lambda u: u["id"] == user_id)
    return results[0] if results else None
