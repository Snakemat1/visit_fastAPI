from sqlalchemy.orm import Session
from database import Project, Message

def get_projects(db: Session):
    return db.query(Project).all()

def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def create_message(db: Session, name: str, email: str, message: str):
    msg = Message(name=name, email=email, message=message)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg

