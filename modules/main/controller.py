from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

routes = APIRouter(tags=["Main"])

templates = Jinja2Templates(directory="modules/main/views")


@routes.get("/", response_class=HTMLResponse)
async def index(request: Request):

    return templates.TemplateResponse(
        "index.html", {"request": request}
    )
