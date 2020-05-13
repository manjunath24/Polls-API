from datetime import datetime

from pydantic import BaseModel
from typing import List


# Choice schema

class ChoiceBase(BaseModel):
	choice_text: str
	votes: int = 0

class ChoiceCreate(ChoiceBase):
	pass

class ChoiceList(ChoiceBase):
	id: int

	class Config:
		orm_mode = True


# Question schema

class QuestionBase(BaseModel):
	question_text: str
	pub_date: datetime

class QuestionCreate(QuestionBase):
	pass

class Question(QuestionBase):
	id: int

	class Config:
		orm_mode = True

class QuestionInfo(Question):
	choices: List[ChoiceList] = []


