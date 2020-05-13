from fastapi import FastAPI, HTTPException, Response, Depends
import schema
from typing import List

from sqlalchemy.orm import Session

import crud
from database import SessionLocal, engine
from models import Base

Base.metadata.create_all(bind=engine)


app = FastAPI()

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


## Question

@app.post("/questions/", response_model=schema.QuestionInfo)
def create_question(question: schema.QuestionCreate, db: Session = Depends(get_db)):
	return crud.create_question(db=db, question=question)


@app.get("/questions/", response_model=List[schema.Question])
def get_questions(db: Session = Depends(get_db)):
	return crud.get_all_questions(db=db)

@app.get("/questions/{qid}", response_model=schema.QuestionInfo)
def get_question(qid: int, db: Session = Depends(get_db)):
	q = crud.get_question(db=db, qid=qid)
	if not q:
		raise HTTPException(status_code=404, detail="Question not found")
	return crud.get_question(db=db, qid=qid)

@app.put("/questions/{qid}", response_model=schema.QuestionInfo)
def edit_question(qid: int, question: schema.QuestionCreate, db: Session = Depends(get_db)):
	q = crud.get_question(db=db, qid=qid)
	if not q:
		raise HTTPException(status_code=404, detail="Question not found")
	obj = crud.edit_question(db=db, qid=qid, question=question)
	return obj

@app.delete("/questions/{qid}", response_model=schema.QuestionInfo)
def delete_question(qid: int, db: Session = Depends(get_db)):
	q = crud.get_question(db=db, qid=qid)
	if not q:
		raise HTTPException(status_code=404, detail="Question not found")
	crud.delete_question(db=db, qid=qid)
	return q


# Choice

@app.post("/questions/{qid}/choice", response_model=schema.ChoiceList)
def create_choice(qid: int, choice: schema.ChoiceCreate, db: Session = Depends(get_db)):
	question = crud.get_question(db=db, qid=qid)
	if not question:
		raise HTTPException(status_code=404, detail="Question not found")
	return crud.create_choice(db=db, qid=qid, choice=choice)

@app.put("/choices/{choice_id}/vote", response_model=schema.ChoiceList)
def update_vote(choice_id: int, db: Session = Depends(get_db)):
	return crud.update_vote(choice_id=choice_id, db=db)

