from datetime import datetime
from pydantic import validator

from pydantic import BaseModel


class NumberOfQuestions(BaseModel):
    question_num: int
    
    @validator("question_num", pre=True)
    def check_number(cls, number):
        if number < 0:
            return ValueError()
        return number


class Question(BaseModel):
    id: int
    text: str
    answer: str
    created_at: datetime
