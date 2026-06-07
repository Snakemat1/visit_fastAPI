from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import api, pages


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(api.router)
app.include_router(pages.router)
