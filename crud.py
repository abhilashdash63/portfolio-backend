from sqlalchemy.orm import Session
import models, schemas

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_projects(db: Session):
    return db.query(models.Project).all()


def get_profile(db: Session):
    return db.query(models.Profile).first()

def get_experience(db: Session):
    return db.query(models.Experience).all()

def get_skills(db: Session):
    return db.query(models.Skill).all()

