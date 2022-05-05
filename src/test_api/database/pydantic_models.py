from datetime import datetime
from pydantic import BaseModel


class NumberOfQuestions(BaseModel):
    question_num: int


class Question(BaseModel):
    id: int
    text: str
    answer: str
    created_at: datetime
