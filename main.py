from fastapi import FastAPI
from routes import listing_routes, user_routes

app = FastAPI(title="Mock Firebase with TinyDB")

# Register routers
app.include_router(user_routes.router)
app.include_router(listing_routes.router)

@app.get("/")
def root():
    return {"message": "Mock Firebase API running"}
