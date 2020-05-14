from sqlalchemy.orm import Session

from models import Base, Question, Choice
import schema

# Question

def create_question(db: Session, question: schema.QuestionCreate):
	obj = Question(**question.dict())
	db.add(obj)
	db.commit()
	return obj

def get_all_questions(db: Session):
	return db.query(Question).all()

def get_question(db:Session, qid):
	return db.query(Question).filter(Question.id == qid).first()

def edit_question(db: Session, qid, question: schema.QuestionCreate):
	obj = db.query(Question).filter(Question.id == qid).first()
	obj.question_text = question.question_text
	obj.pub_date = question.pub_date
	db.commit()
	return obj

def delete_question(db: Session, qid):
	db.query(Question).filter(Question.id == qid).delete()
	db.commit()


# Choice


def create_choice(db:Session, qid: int, choice: schema.ChoiceCreate):
	obj = Choice(**choice.dict(), question_id=qid)
	db.add(obj)
	db.commit()
	return obj

def update_vote(choice_id: int, db:Session):
	obj = db.query(Choice).filter(Choice.id == choice_id).first()
	obj.votes += 1
	db.commit()
	return obj