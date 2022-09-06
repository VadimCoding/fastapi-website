import os
from fastapi import Request, APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ..library.helpers import *


templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("/movies", response_class=HTMLResponse)
async def movie(request: Request):
    data = openfile('movies.md')
    return templates.TemplateResponse("page.html", {"request": request, "data": data})