from sqlalchemy import Column, Integer, Date, String

from database.database import Base, engine


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer(), primary_key=True)
    text = Column(String())
    answer = Column(String())
    created_at = Column(Date())


Base.metadata.create_all(engine)
