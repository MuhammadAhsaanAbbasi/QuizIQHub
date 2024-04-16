from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from quiz_backend.db.db_connector import  createTable
from contextlib import asynccontextmanager
from quiz_backend.utils.exception import NotFoundException, ConflictException, InvalidInputException
from quiz_backend.controllers.user_controllers import signupFn, loginFn
from typing import Annotated
from .utils.exception import NotFoundException, ConflictException, InvalidInputException


# Define async context manager for application lifespan
@asynccontextmanager
async def lifeSpan(app: FastAPI):
    """
    Async context manager to handle application lifespan events.

    Args:
        app (FastAPI): The FastAPI application instance.

    Yields:
        None: Nothing is yielded.
    """
    print("Creating tables...")
    createTable()
    yield

# Create FastAPI application instance with custom lifespan event handler
app = FastAPI(title="OAuth2 Microservice",
    description="A multi-user OAuth2 microservice with login/password signin and Google signin features.",
    version="1.0.0",
    terms_of_service="https://quiz_app.vercel.app/terms/",
    lifespan=lifeSpan,
    contact={
        "name": "Muhammad Ahsaan Abbasi",
        "url": "http://localhost:8000/contact/",
        "email": "mahsaanabbasi@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    },
    servers=[
        {
            "url": "http://localhost:8000",
            "description": "Local server"
        },
    ],)

# add middleware for cors error
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

# Exception handlers for custom exceptions

@app.exception_handler(NotFoundException)
def not_found(request: Request, exception: NotFoundException):
    """
    Exception handler for NotFoundException.

    Args:
        request (Request): The HTTP request.
        exception (NotFoundException): The NotFoundException instance.

    Returns:
        JSONResponse: JSON response with 404 status code and error message.
    """
    return JSONResponse(status_code=400, content=f"{exception.not_found} Not found")

@app.exception_handler(ConflictException)
def conflict_exception(request: Request, exception: ConflictException):
    """
    Exception handler for ConflictException.

    Args:
        request (Request): The HTTP request.
        exception (ConflictException): The ConflictException instance.

    Returns:
        JSONResponse: JSON response with 404 status code and error message.
    """
    return JSONResponse(status_code=409, content=f"This {exception.conflict_input} already exists!")

@app.exception_handler(InvalidInputException)
def invalid_exception(request: Request, exception: InvalidInputException):
    """
    Exception handler for InvalidInputException.

    Args:
        request (Request): The HTTP request.
        exception (InvalidInputException): The InvalidInputException instance.

    Returns:
        JSONResponse: JSON response with 404 status code and error message.
    """
    return JSONResponse(status_code=400, content=f"Invalid {exception.invalid_input}!")

# Define route for home endpoint
@app.get("/")
def home():
    """
    Route for home endpoint.

    Returns:
        str: Welcome message.
    """
    return "Welcome to the Quiz Project..."



@app.post("/api/userSignup")
def userSignup(tokens_data: Annotated[dict, Depends(signupFn)]):
    if not tokens_data:
        raise NotFoundException("User")
    return tokens_data    

@app.post("/api/Signin")
def userSignin(token_data: Annotated[dict, Depends(loginFn)]):
    if token_data:
        return token_data
    raise NotFoundException("User")



# @app.get("/api/getUser")
# def getUser(user: str):
#     """
#     Route to get user details.

#     Args:
#         user (str): User identifier.

#     Returns:
#         str: Success message if user found, else raises NotFoundException.
#     """
#     if user == "bilal":
#         raise NotFoundException("User")
#     return "User has been found"
