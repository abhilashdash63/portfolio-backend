from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Portfolio API Running"}

@app.post("/projects/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db, project)

@app.get("/projects/", response_model=list[schemas.Project])
def read_projects(db: Session = Depends(get_db)):
    return crud.get_projects(db)



@app.get("/profile/", response_model=schemas.Profile)
def read_profile(db: Session = Depends(get_db)):
    return crud.get_profile(db)


@app.get("/experience/", response_model=list[schemas.Experience])
def read_experience(db: Session = Depends(get_db)):
    return crud.get_experience(db)


@app.get("/skills/", response_model=list[schemas.Skill])
def read_skills(db: Session = Depends(get_db)):
    return crud.get_skills(db)
