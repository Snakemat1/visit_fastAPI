from fastapi import APIRouter, HTTPException, Depends

from pydantic import BaseModel
import crud
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix="/api", tags = ["api"])


class Project(BaseModel):
    id: int
    title: str
    stack: list[str]

class ContactForm(BaseModel):
    name: str
    email: str
    message: str

@router.get("/about")
def about():
    return {
        "name": "Timur",
        "profession": "Python Developer",
        "skills": ["Python(python-telegram-bot, Pydantic, pytest)", "GIT", "FastAPI", "Docker", "Redis", "PostgreSQL"],
    }

projects = [
    {"id": 1, "title": "Бот знакомств", "description": "Аналог популярного бота знакомств 'Дайвинчик'. ", "stack": ["Python", "python-telegram-bot", "redis", "PostgreSQL", "pytest", "pydantic", "Alembic", "SQLalchemi", "Docker"], "github": "https://github.com/Snakemat1/tinder"},
    {"id": 2, "title": "Сайт-визитка", "description": "Персональный сайт-портфолио на FastAPI с Jinja2-шаблонами, статикой и формой обратной связи.",    "stack": ["FastAPI", "Jinja2", "Python", "Pydantic"], "github": "https://github.com/Snakemat1/visit_fastAPI"},
]

@router.get("/project/{project_id}")
def get_project(project_id: int, db: Session = Depends(get_db)):
    return crud.get_project(db, project_id)
  
    
@router.get("/projects")
def get_projects(db: Session = Depends(get_db)):
    return crud.get_projects(db)


@router.post("/contact")
def contact(form: ContactForm, db: Session = Depends(get_db)):
    return crud.create_message(db, form.name, form.email, form.message)



