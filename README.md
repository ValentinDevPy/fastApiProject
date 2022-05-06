# FastApi test_project

## Данный проект подготовлен в рамках тестового задания на позицию Junior Python Backend Developer.

FastApi test_project это API с одним эндпоинтом, отправив POST запрос на
который можно получить необходимое количество загадок и сохранить их в БД.
Проект использует FastAPI с SQLAlchemy ORM и Postgresql в качестве БД. 

## Технологии

- [FastAPI](https://github.com/tiangolo/fastapi) - фреймворк, который включает в себя все необходимое для быстрой разработки
самых разнообразных API.
- [Docker и Docker Compose](https://www.docker.com/) - ПО, позволяющее быстро разворачивать свои проекты на различных машинах.


## Начало работы

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ValentinDevPy/fastApiProject.git
```

```
cd fastApiProject

```

Выполнить следующую команду(должны быть установлены Docker и Docker Compose):

```
docker-compose up
```

После этого проект соберется и запустится на вашем компьютере.


Единственный эндпоинт(Принимает только POST запрос) проекта будет доступен по адресу:
```
http://localhost:8008/questions
```


## Примеры работы с API:

Создание необходимого количества вопросов в БД можно осуществить отправив POST запрос на эндпоинт:
```
http://localhost:8008/questions
```
С телом запроса:

```
{
    "question_num": {number_of_questions}
}
```
где {number_of_quetstions} - целое натуральное число.

Пример ответа:
```
[
    {
        "id": 100148,
        "text": "The Chinese discovered that this practice using needles could work as an anesthetic",
        "answer": "acupuncture",
        "created_at": "2014-02-14T02:06:18.023000+00:00"
    }
]

```

## Лицензия

**MIT**

**Free Software, Hell Yeah!**
