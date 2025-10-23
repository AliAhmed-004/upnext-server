import uuid
from .database_service import posts_db

def add_post(post_data):
    post_id = str(uuid.uuid4())
    data = {"id": post_id, **post_data}
    posts_db.insert(data)
    return data

def get_posts_by_user(user_id):
    return posts_db.search(lambda p: p["user_id"] == user_id)

def get_all_posts():
    return posts_db.all()
