from typing import List

from fastapi import APIRouter

from database import db_models
from database.database import Session
from database.pydantic_models import Question, NumberOfQuestions
from .services import (
    get_question_from_api, get_necessary_data_about_question,
    get_unique_questions,
)

router = APIRouter()


@router.post("/questions/", response_model=List[Question])
async def create_questions(number: NumberOfQuestions):
    """Получаем в теле запроса количество необходимых вопросов."""
    response = get_question_from_api(number)
    questions_list = get_necessary_data_about_question(response)
    # Создаем список из уникальных вопросов
    unique_questions_list = get_unique_questions(questions_list)
    session = Session()
    session.bulk_save_objects(
        [
            db_models.Question(
                id=question.id,
                text=question.text,
                answer=question.answer,
                created_at=question.created_at
            )
            for question in questions_list
        ]
    )
    session.commit()
    return unique_questions_list
