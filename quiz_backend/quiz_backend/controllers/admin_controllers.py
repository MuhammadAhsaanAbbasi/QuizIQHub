from typing import Annotated
from passlib.context import CryptContext
from quiz_backend.db.db_connector import get_session
from quiz_backend.setting import admin_name, admin_password
from quiz_backend.models.quiz_models import Category, QuizModel
from sqlmodel import SQLModel, Session, select
from fastapi import Depends, HTTPException, Response
from quiz_backend.models.quiz_models import QuizLevel, Quiz, Choices
from quiz_backend.utils.exception import ConflictException


class Admin(SQLModel):
    admin_name: str
    admin_password: str


pwd = CryptContext(schemes="bcrypt")


def admin_login(admin_details: Admin, response: Response):
    if admin_details.admin_name == admin_name:
        if pwd.verify(admin_details.admin_password, admin_password):
            response.set_cookie('email', admin_name, max_age=300)
            return {'message': 'You are login'}
        else:
            raise HTTPException(status_code=404, detail="Password is Invalid")
    else:
        raise HTTPException(status_code=404, detail="Email is Invalid")


def is_name(session: Session, catgory_name: str):
    # category = Category.category_name.lower()
    statment = select(Category).where(catgory_name.lower() == Category.category_name)
    result = session.exec(statment).first()
    if result:
        return True
    else:
        return False


def set_category(category: Category, session: Annotated[Session, Depends(get_session)]):
    print(category)
    is_exist = is_name(session=session, catgory_name=category.category_name)
    if is_exist:
        raise ConflictException("Category")
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


def is_quiz_level(session: Session, quiz_level_name: str, category_id: int):
    statment = select(QuizLevel).where(category_id == QuizLevel.category_id).where(
        quiz_level_name == QuizLevel.quiz_level)
    result = session.exec(statment).first()
    if result:
        print(result)
        return True
    else:
        return False


def set_quiz_level(admin_quiz_level_input: QuizLevel, session: Annotated[Session, Depends(get_session)]):
    is_exist = is_quiz_level(
        session, admin_quiz_level_input.quiz_level, admin_quiz_level_input.category_id)
    if is_exist:
        raise HTTPException(status_code=404, detail="Already Exist")
    else:
        session.add(admin_quiz_level_input)
        session.commit()
        session.refresh(admin_quiz_level_input)
        return admin_quiz_level_input


# ==============================================================================================================
# def set_questions(admin_question_input : Quiz , session : Annotated[Session , Depends(get_session)]):
#     session.add(admin_question_input)
#     session.commit()
#     session.refresh(admin_question_input)
    # return admin_question_input

# def set_choice(admin_choices_input:Choices ,  session : Annotated[Session , Depends(get_session)]):
#     session.add(admin_choices_input)
#     session.commit()
#     session.refresh(admin_choices_input)
#     return admin_choices_input
# ==============================================================================================================


def set_questions(admin_question_input: QuizModel, session: Annotated[Session, Depends(get_session)]):

    choice01 = Choices(choice=admin_question_input.choice1,
                       status=admin_question_input.choice1_status)
    choice02 = Choices(choice=admin_question_input.choice2,
                       status=admin_question_input.choice2_status)
    choice03 = Choices(choice=admin_question_input.choice3,
                       status=admin_question_input.choice3_status)

    question = Quiz(question=admin_question_input.question,
                    quizLevel_id=admin_question_input.quiz_level_id, questions=[choice01, choice02, choice03])

    session.add(question)
    session.commit()
    session.refresh(question)
    print(admin_question_input)

    return "admin_question_input"
