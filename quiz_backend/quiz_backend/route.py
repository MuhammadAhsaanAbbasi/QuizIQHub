from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from quiz_backend.db.db_connector import get_session, createTable
from contextlib import asynccontextmanager
from quiz_backend.models.user_models import User
from quiz_backend.utils.imports import NotFoundException
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


@app.exception_handler(NotFoundException)
def not_found(request: Request, exception: NotFoundException):
    return JSONResponse(status_code=404, content=f"{exception.not_found} Not found")


# Define route for home endpoint
@app.get("/")
def home():
    return "Welcome to the Quiz Project..."


@app.get("/api/getUser")
def getUser(user: str):
    if user == "bilal":
        raise NotFoundException("User")
    return "User has found"
