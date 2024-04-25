from sqlmodel import Session, select, func
from quiz_backend.models.quiz_models import Category, QuizLevel, Quiz,  Choices


def get_categrios(session: Session):
    catergories = session.exec(select(Category)).all()
    return catergories


def get_quiz_diff(session: Session, category_id: int):
    statment = select(QuizLevel).where(category_id == QuizLevel.category_id)
    quiz_level = session.exec(statment).all()
    return quiz_level


def get_choices(question_id: int | None, session: Session):
    statment = select(Choices).where(question_id == Choices.quiz_id)
    choices = session.exec(statment).all()
    return choices


def get_question(session: Session):

    # statment = select(Choices).join(Quiz)
    # statment = select(Quiz).join(Choices)
    # statment = select(Quiz).join(Choices, isouter=True)
    # statment = select(Quiz, Choices).join(Choices)

    statment = select(Quiz, Choices).join(Choices, isouter=True)
    questions = session.exec(statment).all()
    # data = []
    # for question in questions:
    #    choices =  get_choices(question.question_id , session)
    #    data.append(

    #     {
    #        "question" : question.question,
    #        'chocies': choices
    #     }

    #    )
    print(questions)
    return "questions"
