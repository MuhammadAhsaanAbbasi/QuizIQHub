from typing import Optional
from sqlmodel import SQLModel, Field

class LoginModel(SQLModel):
    user_email: str
    user_password: str
    

class UserModel(LoginModel):
    user_name: str

# Define User model
class User(UserModel, table=True):
    user_id: Optional[int] = Field(None, primary_key=True)
    # user_name: str  # User's name
    # user_email: str  # User's email address
    # user_password: str  # User's password
    # TODO: Add phone_number field
    # phone_number: int

# Define Token model
class Token(SQLModel, table=True):
    token_id: Optional[int] = Field(None, primary_key=True)
    user_id: int = Field(int, foreign_key="user.user_id")
    refresh_token: str  # Refresh token for authentication
