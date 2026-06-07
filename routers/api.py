from fastapi import APIRouter
from fastapi import HTTPException

from pydantic import BaseModel


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
        "profession": "Python Junior Developer",
        "skills": ["Python", "GIT", "FastAPI"],
    }

projects = [
    {"id": 1, "title": "Мой первый проект", "stack": ["Python", "FastAPI"]},
    {"id": 2, "title": "Второй проект",     "stack": ["Docker"]},
]

@router.get("/project/{project_id}")
def get_project(project_id: int):
    project = next((p for p in projects if p["id"] == project_id), None)
    if project is None:
        raise HTTPException(status_code=404, detail="Проект не найден")
    return project

@router.get("/projects", response_model=list[Project])
def get_projects(limit: int=10):
    return projects[:limit]

@router.post("/contact")
def contact(form: ContactForm):
    if form.name == "" or not form.message.strip():
        raise HTTPException(status_code=400, detail="Имя не может быть пустым")
    return {"status": "ok", "form": form.name}



