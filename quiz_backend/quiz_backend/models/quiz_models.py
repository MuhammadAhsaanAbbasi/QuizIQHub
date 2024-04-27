from typing import Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship


# Define Category model
class Category(SQLModel, table=True):
    category_id: Optional[int] = Field(None, primary_key=True)# It will generate database
    category_name: str  # Name of the category
    category_description: str  # Description of the category


# Define QuizLevel model with foreign key relationship to Category
class QuizLevel(SQLModel, table=True):
    quiz_level_id: Optional[int] = Field(None, primary_key=True)
    quiz_level: str  # Level of the quiz
    category_id: int  = Field(int, foreign_key="category.category_id")  # Foreign key relationship to Category



# Define Quiz model with foreign key relationship to QuizLevel
class Quiz(SQLModel, table=True):
    question_id: Optional[int] = Field(None, primary_key=True)
    question: str  # Question for the quiz
    quizLevel_id: int  = Field(int, foreign_key="quizlevel.quiz_level_id")  # Foreign key relationship to QuizLevel
    questions: list["Choices"] = Relationship(back_populates="choices")

    
    
# Define Choices model with foreign key relationship to Quiz
class Choices(SQLModel, table=True):
    choice_id: Optional[int] = Field(None, primary_key=True)
    quiz_id: int  = Field(int, foreign_key="quiz.question_id")  # Foreign key relationship to Quiz
    choice: str  # Choice for the question
    status: bool = False  # Status of the choice (correct or incorrect)
    choices: Quiz | None = Relationship(back_populates="questions")
 
 
class QuizModel(BaseModel):
    quiz_level_id: int
    question: str
    choice1: str
    choice1_status: bool = False
    choice2: str
    choice2_status: bool = False
    choice3: str
    choice3_status: bool = False
        
