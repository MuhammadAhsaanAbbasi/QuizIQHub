from fastapi import FastAPI
from quiz_backend.db.db_connector import get_session, createTable
from contextlib import asynccontextmanager
from quiz_backend.models.user_models import User

# Import other model modules
import quiz_backend.models.admin_models
import quiz_backend.models.quiz_models

# Define async context manager for application lifespan
@asynccontextmanager
async def lifeSpan(app: FastAPI):
    print("Creating tables...")
    createTable()
    yield

# Create FastAPI application instance with custom lifespan event handler
app = FastAPI(lifespan=lifeSpan)

# Define route for home endpoint
@app.get("/")
def home():
    return "Welcome to the Quiz Project..."
