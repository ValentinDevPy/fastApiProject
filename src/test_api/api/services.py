import requests

from database.pydantic_models import Question
from database import db_models
from database.database import Session


def get_question_from_api(number=1):
    """Получаем ответ от внешнего апи и преобразуем в dict."""
    base_url = 'https://jservice.io/api/random'
    params = {
        'count': number
    }
    response = requests.get(base_url, params=params)
    return response.json()


def get_necessary_data_about_question(api_response):
    """Вытаскиваем из словаря необходимые данные и преобразуем
    Pydantic model."""
    result = []
    for question_obj in api_response:
        question_obj = {
            'id': question_obj.get('id'),
            'text': question_obj.get('question'),
            'answer': question_obj.get('answer'),
            'created_at': question_obj.get('created_at')
        }
        result.append(Question.parse_obj(question_obj))
    return result


def get_unique_questions(list_of_questions):
    """Проверяем нет ли в полученных вопросах тех,
    которые уже записаны в нашу базу,
    если таковые есть то получаем по 1 вопросу до тех пор,
    пока он не окажется уникальным."""
    session = Session()
    ids = {x.id for x in session.query(db_models.Question).all()}
    for i in range(len(list_of_questions)):
        if list_of_questions[i].id in ids:
            while list_of_questions[i].id in ids:
                api_response = get_question_from_api()
                list_of_questions[i] = (
                    get_necessary_data_about_question(api_response)[0]
                )
    return list_of_questions
