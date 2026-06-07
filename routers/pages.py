from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from routers.api import projects

router = APIRouter(tags=["pages"])
templates = Jinja2Templates(directory="templates")

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse(request,"index.html", {
        "name": "Timur",
        "profession": "Python Junior Developer",
        "skills": ["Python(python-telegram-bot, Pydantic, pytest)", "GIT", "FastAPI", "Docker", "Redis", "PostgreSQL"]
    })

@router.get("/portfolio")
async def portfolio(request: Request):
    return templates.TemplateResponse(request, "portfolio.html", {
        "projects": projects,
    })

@router.get("/contact")
async def get_contact(request: Request):
    return templates.TemplateResponse(request, "contact.html", {})