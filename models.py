from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Question(Base):
	__tablename__ = "question"
	id = Column(Integer, primary_key=True)
	question_text = Column(String(200))
	pub_date = Column(DateTime)

	choices = relationship('Choice', back_populates="question")


class Choice(Base):
	__tablename__ = "choice"
	id = Column(Integer, primary_key=True)
	question_id = Column(Integer, ForeignKey('question.id', ondelete='CASCADE'))
	choice_text = Column(String(200))
	votes = Column(Integer, default=0)

	question = relationship("Question", back_populates="choices")