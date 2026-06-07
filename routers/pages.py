from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(tags=["pages"])
templates = Jinja2Templates(directory="templates")

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse(request,"index.html", {
        "name": "Timur",
        "profession": "Python Junior Developer",
        "skills": ["Python", "GIT", "FastAPI"]
    })