from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")


templates = Jinja2Templates(directory="frontend")


links = [
    {"label": "Home", "url": "home"},
    {"label": "Our Menus", "url": "menus"},
    {"label": "Blog Entries", "url": "blogs"},
    {"label": "Contact Us", "url": "contacts"},
]


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request, "links": links})

@app.get("/contacts", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "links": links})

