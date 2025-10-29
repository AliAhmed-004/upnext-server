import uuid
from .database_service import listing_table

def add_post(post_data):
    post_id = str(uuid.uuid4())
    data = {"id": post_id, **post_data}
    listing_table.insert(data)
    return data

def get_posts_by_user(user_id):
    return listing_table.search(lambda p: p["user_id"] == user_id)

def get_all_posts():
    return listing_table.all()
